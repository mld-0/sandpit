
bin_python="/usr/local/bin/python3"
test_results="Test-results.txt"

#	This script works (calling each test either using python or SHELL) because said test scripts work when called from this top-level directory, or within each containing directory

echo "====================" > "$test_results"
echo "Test Results: (Success = 0)" >> "$test_results"
echo $( date "+%FT%H:%M:%S%Z" ) >> "$test_results"

IFS_temp=$IFS
IFS=$'\0'
test_py_files=( $( find . -name 'test.py' -type f -print0 | perl -pE "s/\x00$//" ) )
IFS=$IFS_temp
for loop_file in "${test_py_files[@]}"; do
	$bin_python "$loop_file" 
	echo -n "\t$?\t" >> "$test_results"
	echo "$loop_file" >> "$test_results"
done
echo ""

IFS_temp=$IFS
IFS=$'\0'
test_sh_files=( $( find . -name 'test.sh' -type f -print0 | perl -pE "s/\x00$//" ) )
IFS=$IFS_temp
for loop_file in "${test_sh_files[@]}"; do
	time ( $SHELL "$loop_file" )
	echo -n "\t$?\t" >> "$test_results"
	echo "$loop_file\t" >> "$test_results"
done
echo ""

echo "====================" >> "$test_results"
cat "$test_results"
rm "$test_results"

