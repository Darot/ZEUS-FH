//Author: Domminik Krichbaum

#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <unistd.h>
#include <stdio.h>

#define FILEPATH "/tmp/size"

int main(int argc ,char *argv[])
{
    int fd;
    int result;
    int filesize; 
    
    //Validate Arguments
    if(argc != 2){
      printf("Error invalid or Arguments\n");
      //getchar();
      return 1;
    } else {
      filesize = atoi(argv[1]);
      printf("%d \n", filesize);
    }

    remove(FILEPATH);
    
    fd = open(FILEPATH, O_WRONLY | O_CREAT | O_EXCL, (mode_t)0600);
    if (fd == -1) {
	perror("Error opening file for writing\n");
        return 1;
    }

    /* Stretch the file size.
     * Note that the bytes are not actually written,
     * and cause no IO activity.
     * Also, the diskspace is not even used
     * on filesystems that support sparse files.
     * (you can verify this with 'du' command)
     */
    result = lseek(fd, filesize-1, SEEK_SET);
    if (result == -1) {
	close(fd);
	perror("Error calling lseek() to 'stretch' the file");
        return 1;
    }

    /* write just one byte at the end */
    result = write(fd, "", 1);
    if (result < 0) {
	close(fd);
	perror("Error writing a byte at the end of the file");
        return 1;
    }

    /* do other things here */
    close(fd);
    return 0;
  
}
