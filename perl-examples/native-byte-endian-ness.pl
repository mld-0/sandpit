
use Config;
#	'1234' and '12345678' are little-endian,
#	'4321' and '87654321' are big-endian
print $Config{byteorder}, "\n";

