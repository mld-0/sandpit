#   VIM SETTINGS: {{{3
#   vim: set tabstop=4 modeline modelines=10 foldmethod=marker:
#   vim: set foldlevel=2 foldcolumn=3: 
#   }}}1
import sys
import pprint
import dateutil.parser
import dateparser
import logging
import datetime
#   {{{2

#   (Methods from) dtscan.dtconvert.Convert_string2DateTime (in order):
#       datetime.fromtimestamp(datetime_epoch_str)
#       dateutil.parser.parse(datetime_str)
#       datetime.strptime(datetime_str, trial_format)
#       dateparser.parse(datetime_str, dateformats=trial_formats_list)
#   Given '2020-12-27T11:51:56AEST' as input -> what is resulting timezone / epoch for each function

#   AssumeTimeZone: 
#   {{{
#   check for timezone information (if [...] return result_datetime)
#       if (result_datetime.tzinfo is None) and not isinstance(result_datetime.tzinfo, dateutil.tz.tzoffset):
#   check for timezone information (if [...] return result_datetime)
#       if (isinstance(result_datetime.tzinfo, dateutil.tz.tzoffset)):
#   }}}

#   Writing (better) string2DateTime() and addAssumedTimeZone()


#   timezone_info dict, needed by dateutil.parser.parse to avoid timezone-not-recognised error
#   {{{
timezone_info = {
        "A": 1 * 3600,
        "ACDT": 10.5 * 3600,
        "ACST": 9.5 * 3600,
        "ACT": -5 * 3600,
        "ACWST": 8.75 * 3600,
        "ADT": 4 * 3600,
        "AEDT": 11 * 3600,
        "AEST": 10 * 3600,
        "AET": 10 * 3600,
        "AFT": 4.5 * 3600,
        "AKDT": -8 * 3600,
        "AKST": -9 * 3600,
        "ALMT": 6 * 3600,
        "AMST": -3 * 3600,
        "AMT": -4 * 3600,
        "ANAST": 12 * 3600,
        "ANAT": 12 * 3600,
        "AQTT": 5 * 3600,
        "ART": -3 * 3600,
        "AST": 3 * 3600,
        "AT": -4 * 3600,
        "AWDT": 9 * 3600,
        "AWST": 8 * 3600,
        "AZOST": 0 * 3600,
        "AZOT": -1 * 3600,
        "AZST": 5 * 3600,
        "AZT": 4 * 3600,
        "AoE": -12 * 3600,
        "B": 2 * 3600,
        "BNT": 8 * 3600,
        "BOT": -4 * 3600,
        "BRST": -2 * 3600,
        "BRT": -3 * 3600,
        "BST": 6 * 3600,
        "BTT": 6 * 3600,
        "C": 3 * 3600,
        "CAST": 8 * 3600,
        "CAT": 2 * 3600,
        "CCT": 6.5 * 3600,
        "CDT": -5 * 3600,
        "CEST": 2 * 3600,
        "CET": 1 * 3600,
        "CHADT": 13.75 * 3600,
        "CHAST": 12.75 * 3600,
        "CHOST": 9 * 3600,
        "CHOT": 8 * 3600,
        "CHUT": 10 * 3600,
        "CIDST": -4 * 3600,
        "CIST": -5 * 3600,
        "CKT": -10 * 3600,
        "CLST": -3 * 3600,
        "CLT": -4 * 3600,
        "COT": -5 * 3600,
        "CST": -6 * 3600,
        "CT": -6 * 3600,
        "CVT": -1 * 3600,
        "CXT": 7 * 3600,
        "ChST": 10 * 3600,
        "D": 4 * 3600,
        "DAVT": 7 * 3600,
        "DDUT": 10 * 3600,
        "E": 5 * 3600,
        "EASST": -5 * 3600,
        "EAST": -6 * 3600,
        "EAT": 3 * 3600,
        "ECT": -5 * 3600,
        "EDT": -4 * 3600,
        "EEST": 3 * 3600,
        "EET": 2 * 3600,
        "EGST": 0 * 3600,
        "EGT": -1 * 3600,
        "EST": -5 * 3600,
        "ET": -5 * 3600,
        "F": 6 * 3600,
        "FET": 3 * 3600,
        "FJST": 13 * 3600,
        "FJT": 12 * 3600,
        "FKST": -3 * 3600,
        "FKT": -4 * 3600,
        "FNT": -2 * 3600,
        "G": 7 * 3600,
        "GALT": -6 * 3600,
        "GAMT": -9 * 3600,
        "GET": 4 * 3600,
        "GFT": -3 * 3600,
        "GILT": 12 * 3600,
        "GMT": 0 * 3600,
        "GST": 4 * 3600,
        "GYT": -4 * 3600,
        "H": 8 * 3600,
        "HDT": -9 * 3600,
        "HKT": 8 * 3600,
        "HOVST": 8 * 3600,
        "HOVT": 7 * 3600,
        "HST": -10 * 3600,
        "I": 9 * 3600,
        "ICT": 7 * 3600,
        "IDT": 3 * 3600,
        "IOT": 6 * 3600,
        "IRDT": 4.5 * 3600,
        "IRKST": 9 * 3600,
        "IRKT": 8 * 3600,
        "IRST": 3.5 * 3600,
        "IST": 5.5 * 3600,
        "JST": 9 * 3600,
        "K": 10 * 3600,
        "KGT": 6 * 3600,
        "KOST": 11 * 3600,
        "KRAST": 8 * 3600,
        "KRAT": 7 * 3600,
        "KST": 9 * 3600,
        "KUYT": 4 * 3600,
        "L": 11 * 3600,
        "LHDT": 11 * 3600,
        "LHST": 10.5 * 3600,
        "LINT": 14 * 3600,
        "M": 12 * 3600,
        "MAGST": 12 * 3600,
        "MAGT": 11 * 3600,
        "MART": 9.5 * 3600,
        "MAWT": 5 * 3600,
        "MDT": -6 * 3600,
        "MHT": 12 * 3600,
        "MMT": 6.5 * 3600,
        "MSD": 4 * 3600,
        "MSK": 3 * 3600,
        "MST": -7 * 3600,
        "MT": -7 * 3600,
        "MUT": 4 * 3600,
        "MVT": 5 * 3600,
        "MYT": 8 * 3600,
        "N": -1 * 3600,
        "NCT": 11 * 3600,
        "NDT": 2.5 * 3600,
        "NFT": 11 * 3600,
        "NOVST": 7 * 3600,
        "NOVT": 7 * 3600,
        "NPT": 5.5 * 3600,
        "NRT": 12 * 3600,
        "NST": 3.5 * 3600,
        "NUT": -11 * 3600,
        "NZDT": 13 * 3600,
        "NZST": 12 * 3600,
        "O": -2 * 3600,
        "OMSST": 7 * 3600,
        "OMST": 6 * 3600,
        "ORAT": 5 * 3600,
        "P": -3 * 3600,
        "PDT": -7 * 3600,
        "PET": -5 * 3600,
        "PETST": 12 * 3600,
        "PETT": 12 * 3600,
        "PGT": 10 * 3600,
        "PHOT": 13 * 3600,
        "PHT": 8 * 3600,
        "PKT": 5 * 3600,
        "PMDT": -2 * 3600,
        "PMST": -3 * 3600,
        "PONT": 11 * 3600,
        "PST": -8 * 3600,
        "PT": -8 * 3600,
        "PWT": 9 * 3600,
        "PYST": -3 * 3600,
        "PYT": -4 * 3600,
        "Q": -4 * 3600,
        "QYZT": 6 * 3600,
        "R": -5 * 3600,
        "RET": 4 * 3600,
        "ROTT": -3 * 3600,
        "S": -6 * 3600,
        "SAKT": 11 * 3600,
        "SAMT": 4 * 3600,
        "SAST": 2 * 3600,
        "SBT": 11 * 3600,
        "SCT": 4 * 3600,
        "SGT": 8 * 3600,
        "SRET": 11 * 3600,
        "SRT": -3 * 3600,
        "SST": -11 * 3600,
        "SYOT": 3 * 3600,
        "T": -7 * 3600,
        "TAHT": -10 * 3600,
        "TFT": 5 * 3600,
        "TJT": 5 * 3600,
        "TKT": 13 * 3600,
        "TLT": 9 * 3600,
        "TMT": 5 * 3600,
        "TOST": 14 * 3600,
        "TOT": 13 * 3600,
        "TRT": 3 * 3600,
        "TVT": 12 * 3600,
        "U": -8 * 3600,
        "ULAST": 9 * 3600,
        "ULAT": 8 * 3600,
        "UTC": 0 * 3600,
        "UYST": -2 * 3600,
        "UYT": -3 * 3600,
        "UZT": 5 * 3600,
        "V": -9 * 3600,
        "VET": -4 * 3600,
        "VLAST": 11 * 3600,
        "VLAT": 10 * 3600,
        "VOST": 6 * 3600,
        "VUT": 11 * 3600,
        "W": -10 * 3600,
        "WAKT": 12 * 3600,
        "WARST": -3 * 3600,
        "WAST": 2 * 3600,
        "WAT": 1 * 3600,
        "WEST": 1 * 3600,
        "WET": 0 * 3600,
        "WFT": 12 * 3600,
        "WGST": -2 * 3600,
        "WGT": -3 * 3600,
        "WIB": 7 * 3600,
        "WIT": 9 * 3600,
        "WITA": 8 * 3600,
        "WST": 14 * 3600,
        "WT": 0 * 3600,
        "X": -11 * 3600,
        "Y": -12 * 3600,
        "YAKST": 10 * 3600,
        "YAKT": 9 * 3600,
        "YAPT": 10 * 3600,
        "YEKST": 6 * 3600,
        "YEKT": 5 * 3600,
        "Z": 0 * 3600,
}
#   }}}

tests_dt = [ '2020-12-27T11:51:56AEST', '2020-12-27T12:51:56AEDT'  ]
check_epoch = '1609033916.0'
test_datetime_format = "%Y-%m-%dT%H:%M:%S%Z"

#import pytz # $ pip install pytz
#{tzname for tz in map(pytz.timezone, pytz.all_timezones) 
#for _, _, tzname in getattr(tz, '_transition_info', [])}

#   Parsing datetime using <various> 
for loop_test_dt in tests_dt:
    results_dt = []
    results_epoch = []
    loop_output_str = ""

    _result = dateparser.parse(loop_test_dt, settings={'RETURN_AS_TIMEZONE_AWARE': True})
    results_dt.append(_result)
    results_epoch.append(_result.timestamp())

    _result = dateutil.parser.parse(loop_test_dt, tzinfos=timezone_info)
    results_dt.append(_result)
    results_epoch.append(_result.timestamp())

    #_result = datetime.datetime.strptime(_result.strftime(test_datetime_format), test_datetime_format)

    sys.stderr.write("loop_test_dt=(%s)\n" % str(loop_test_dt))
    sys.stderr.write("check_epoch=(%s)\n" % str(check_epoch))
    loop_output_str += "results_dt:\n%s\n" % pprint.pformat(results_dt)
    for loop_line in loop_output_str.strip().split("\n"):
        sys.stderr.write("\t%s\n" % loop_line)
    sys.stderr.write("\n")
    #   Verify each item in results_dt is equal to next item in list
    for loop_i in range(0, len(results_dt)-1):
        assert results_dt[loop_i] == results_dt[loop_i+1], "results not equal for loop_i=(%s)" % str(loop_i)
    #   Verify each item in results_dt, when convert to string using test_datetime_format, is equal to loop_test_dt
    for loop_result_dt in results_dt:
        loop_result_dt_str = loop_result_dt.strftime(test_datetime_format) 
        assert loop_result_dt_str == loop_test_dt, "loop_result_dt=(%s) != loop_test_dt" % loop_result_dt_str
    #   Verify each item in results_epoch (as string) is equal to check_epoch
    for loop_result_epoch in results_epoch:
        assert str(loop_result_epoch) == check_epoch, "loop_result_epoch=(%s) != check_epoch" % str(loop_result_epoch)

#   Parsing datetime using <various> and format test_datetime_format
for loop_test_dt in tests_dt:
    results_dt = []
    results_epoch = []
    loop_output_str = ""

    #   Ongoing: 2020-12-28T17:55:37AEST datetime.strptime(datetime, format) does not support all named timezones (%Z)

    _result = dateparser.parse(loop_test_dt, date_formats=[ test_datetime_format ],  settings={'RETURN_AS_TIMEZONE_AWARE': True})
    results_dt.append(_result)
    results_epoch.append(_result.timestamp())

    #   Ongoing: 2020-12-28T18:33:52AEST custom format for dateutil.parser.parse()?

    sys.stderr.write("loop_test_dt=(%s)\n" % str(loop_test_dt))
    sys.stderr.write("check_epoch=(%s)\n" % str(check_epoch))
    loop_output_str += "results_dt:\n%s\n" % pprint.pformat(results_dt)
    for loop_line in loop_output_str.strip().split("\n"):
        sys.stderr.write("\t%s\n" % loop_line)
    sys.stderr.write("\n")
    #   Verify each item in results_dt is equal to next item in list
    for loop_i in range(0, len(results_dt)-1):
        assert results_dt[loop_i] == results_dt[loop_i+1], "results not equal for loop_i=(%s)" % str(loop_i)
    #   Verify each item in results_dt, when convert to string using test_datetime_format, is equal to loop_test_dt
    for loop_result_dt in results_dt:
        loop_result_dt_str = loop_result_dt.strftime(test_datetime_format) 
        assert loop_result_dt_str == loop_test_dt, "loop_result_dt=(%s) != loop_test_dt" % loop_result_dt_str
    #   Verify each item in results_epoch (as string) is equal to check_epoch
    for loop_result_epoch in results_epoch:
        assert str(loop_result_epoch) == check_epoch, "loop_result_epoch=(%s) != check_epoch" % str(loop_result_epoch)






#   }}}1

