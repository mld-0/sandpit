#include <stdio.h>     /* for printf */
#include <stdlib.h>    /* for exit */
#include <getopt.h>    /* for getopt_long; POSIX standard getopt is in unistd.h */

//	TODO: 2021-06-07T19:22:01AEST A more concise (useful) example, on the usage of getopt(), getopt_long()

void print_help();

int main (int argc, char **argv) 
{
    int c;
    int digit_optind = 0;
    int aopt = 0, bopt = 0;
    char *copt = 0, *dopt = 0;
    static struct option long_options[] = {
    /*   NAME       ARGUMENT           FLAG  SHORTNAME */
		{"help", 	no_argument,       NULL, 'h'},
        {"add",     required_argument, NULL, 0},
        {"append",  no_argument,       NULL, 0},
        {"delete",  required_argument, NULL, 0},
        {"verbose", no_argument,       NULL, 0},
        {"create",  required_argument, NULL, 'c'},
        {"file",    required_argument, NULL, 0},
        {NULL,      0,                 NULL, 0}
    };
    int option_index = 0;
    while ((c = getopt_long(argc, argv, "habc:d:012", long_options, &option_index)) != -1) {
        int this_option_optind = optind ? optind : 1;
        switch (c) {
        	case 0:
        	    printf ("option %s", long_options[option_index].name);
        	    if (optarg)
        	        printf (" with arg %s", optarg);
        	    printf ("\n");
        	    break;
        	case '0':
        	case '1':
        	case '2':
        	    if (digit_optind != 0 && digit_optind != this_option_optind)
        	      printf ("digits occur in two different argv-elements.\n");
        	    digit_optind = this_option_optind;
        	    printf ("option %c\n", c);
        	    break;
        	case 'a':
        	    printf ("option a\n");
        	    aopt = 1;
        	    break;
        	case 'b':
        	    printf ("option b\n");
        	    bopt = 1;
        	    break;
        	case 'c':
        	    printf ("option c with value '%s'\n", optarg);
        	    copt = optarg;
        	    break;
        	case 'd':
        	    printf ("option d with value '%s'\n", optarg);
        	    dopt = optarg;
        	    break;
			case 'h':
				print_help();
				exit(EXIT_SUCCESS);
        	case '?':
        	    break;
        	default:
        	    printf ("?? getopt returned character code 0%o ??\n", c);
        }
    }
    if (optind < argc) {
        printf ("non-option ARGV-elements: ");
        while (optind < argc)
            printf ("%s ", argv[optind++]);
        printf ("\n");
    }
    exit (0);
}

void print_help()
{
	const char *help_message = "Options:\n\
	-h | --help                Show this message\n\
	-a\n\
	-b\n\
	-c | --create [value]\n\
	-d [value]\n\
	--add [value]\n\
	--append\n\
	--delete [value]\n\
	--verbose\n\
	--file [value]\n\
	-0\n\
	-1\n\
	-2";
	printf("%s\n", help_message);
}

