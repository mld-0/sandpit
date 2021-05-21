#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>
#include <time.h>

#define RAND_VALS_COUNT 100

//	Creation of temporary directory
//	LINK: https://stackoverflow.com/questions/18792489/how-to-create-a-temporary-directory-in-c
//	TODO: 2021-05-21T19:48:59AEST behaviour/alternative on Windows?

int main() 
{
	int tempdir_delete = 1;
	char tempdir_template[] = "/tmp/c-rand-data.XXXXXX";
	char *tempdir_path = mkdtemp(tempdir_template);
	char *outfile_name = "random-data.txt";

	int max_rand = 100;
	int min_rand = 0;

	if (tempdir_path == NULL) {
		perror("mkdtemp failed: ");
		exit(2);
	}
	printf("Create tempdir_path=(%s)\n", tempdir_path);

	char outfile_path[1024];
	sprintf(outfile_path, "%s/%s", tempdir_path, outfile_name);
	printf("outfile_path=(%s)\n", outfile_path);

	//	Seed rng
	srand(time(NULL));

	FILE *f;
	f = fopen(outfile_path, "w");
	if (f == NULL) {
		fprintf(stderr, "fopen error\n");
		exit(2);
	}

	int loop_rand;
	for (int i = 0; i < RAND_VALS_COUNT; ++i) {
		// Use of rand() to get integers in range [min_rand, max_rand)
		loop_rand = (rand() % (max_rand - min_rand)) + min_rand;
		fprintf(f, "%d\n", loop_rand);
	}
	fclose(f);

	//	Deleting a non-empty directory is a non-trival task? <- so we delete the file inside first. 
	//	Deleting all files in a dir recursively (in C) is a PITA?
	//	Delete temp dir (if tempdir_delete != 0)
	if (tempdir_delete != 0) {
		if (remove(outfile_path) != 0) {
			perror("remove failed: ");
			exit(2);
		} else {
			printf("deleted outfile_path\n");
		}
		if (rmdir(tempdir_path) == -1) {
			perror("rmdir failed: ");
			exit(2);
		} else {
			printf("deleted tempdir_path\n");
		}
	}

	return 0;
}
