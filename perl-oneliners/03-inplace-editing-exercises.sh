
#	Replace s/in/an/ in text.txt
echo "a)"
if [[ -e "text.txt.orig" ]]; then mv "text.txt.orig" "text.txt"; fi
perl -i'.orig' -pE 's/in/an/g' "text.txt";
cat "text.txt"
echo ""

#	b): as per a), but without '.orig' value for -i flag

#	Replace s/copyright: 2018/copyright: 2020/ in copyright.txt
echo "c)"
if [[ -e "2018_copyright.txt.bkp" ]]; then mv "2018_copyright.txt.bkp" "copyright.txt"; fi
perl -i'2018_*.bkp' -pE 's/copyright: 2018/copyright: 2020/g' "copyright.txt"
cat "copyright.txt"
echo ""

#	d): 
#	Expectation: 	
#		In the code sample shown below, two files are created by redirecting output of echo command. Then a perl command is used to edit b1.txt in-place as well as create a backup named   .
# echo '2 apples' > b1.txt
# echo '5 bananas' > -ibkp.txt
# perl -ibkp.* -pe 's/2/two/' b1.txt
#	Issue ... (guessing that) no quoting of value to -i flag is a problem? <- (or) (what is with) having a file named '-ibkp.txt'?
#	Ans: 
#		Unquoted strings on the command line are subjected to shell interpretation. So, -ibkp.* will get expanded as -ibkp.txt (as there exists a file whose name starts with -ibkp.). This results in back up filename as b1.txtbkp.txt (because bkp.txt will be treated as the suffix to be added to input file b1.txt). 
#		The correct usage to get bkp.b1.txt as the back up filename is:
#			perl -i'bkp.*' -pe 's/2/two/' b1.txt 

