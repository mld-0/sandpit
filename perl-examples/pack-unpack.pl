#!/usr/env/bin perl
use strict;
use warnings;
use v5.032;

#	result is "\000\006hello,\005world"
my $result = pack('n/a* w/a*','hello,','world');  
say "result=($result)";

my $foo = pack("CCCC", (65,66,67,68));
say "foo=($foo)";

#	Encode 'ⒶⒷⒸⒹ'
$foo = pack("U4",0x24b6,0x24b7,0x24b8,0x24b9);
say "foo=($foo)";
say "";

#	Encode '😀'
$foo = pack("U4", 0xf0, 0x9f, 0x98, 0x80);
say "foo=($foo)";
say "";

#	Decode '😀'
#	as binary (use b for lowest bit first)
$foo = unpack("B*", '😀');
say "foo=($foo)";
#	as hex (use h for lowest digit first)
$foo = unpack("H*", '😀');
say "foo=($foo)";
say "";

my $emoji_hex_str = unpack("H*", '😀');

#	Convert unpack results (hex-string of smiling emoji) to byte-array:
my @emoji_hex_pairs = ($emoji_hex_str =~ /(..)/g);
my @emoji_hex_values = map({ hex($_) } @emoji_hex_pairs);
my @emoji_bytes = map({ pack('C', $_) } @emoji_hex_values);
say (scalar @emoji_bytes);
#	or (produces byte-array)
@emoji_bytes = map({ pack('C', hex($_)) } ($emoji_hex_str =~ /(..)/g));
say (scalar @emoji_bytes);
#	or (produces string)
@emoji_bytes = pack "H*", $emoji_hex_str;


#	Set LIST_SEPERATOR to '' -> printing of @emoji_bytes will result in printing of emoji
$" = '';
say "emoji_hex_pairs=(@emoji_hex_pairs)";
say "emoji_hex_values=(@emoji_hex_values)";
say "emoji_bytes=(@emoji_bytes)";
say "";

