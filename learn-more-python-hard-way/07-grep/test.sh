
bin_python=/usr/local/bin/python3
test_script_grep="implement-grep.py"
test_dir=data_test

test_script() {
	local disregard_stderr=1
	echo "test_args=(${test_args[@]})"
	local test_result="";
	local test_check="";
	if [[ ! $disregard_stderr -eq 0 ]]; then
		test_result=$( $bin_python $test_script_grep ${test_args[@]} 2> /dev/null )
		test_check=$( grep ${test_args[@]} 2> /dev/null )
	else
		test_result=$( $bin_python $test_script_grep ${test_args[@]} )
		test_check=$( grep ${test_args[@]} )
	fi
	if [[ ! "$test_result" == "$test_check" ]]; then
		echo "Failed, test_result != test_check"
		#echo "test_result=($test_result)"
		#echo "test_check=($test_check)"
		diff <( echo "$test_result" ) <( echo "$test_check" )
	else
		echo "test succeded"
	fi
}

test_args=( "a" "$test_dir/fruit.txt" )
test_script "$test_args"
echo ""

test_args=( "abc" "$test_dir/equns.txt" "$test_dir/fruit.txt" "$test_dir/msg.txt" "$test_dir/paragraphs.txt" "$test_dir/paths.txt" "$test_dir/poem.txt" "$test_dir/range.txt" "$test_dir/replace-test.txt" "$test_dir/report.txt" "$test_dir/values.csv" )
test_script "$test_args"
echo ""

test_args=( "-v" "abc" "$test_dir/equns.txt" "$test_dir/fruit.txt" "$test_dir/msg.txt" "$test_dir/paragraphs.txt" "$test_dir/paths.txt" "$test_dir/poem.txt" "$test_dir/range.txt" "$test_dir/replace-test.txt" "$test_dir/report.txt" "$test_dir/values.csv" )
test_script "$test_args"
echo ""

test_args=( "abc" "$test_dir/*" )
test_script "$test_args"

