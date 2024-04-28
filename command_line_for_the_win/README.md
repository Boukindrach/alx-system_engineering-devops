==================================

Command Line For Win Challenge

==================================


## Steps to Transfer Command line Chellage pictures Using SFTP

1. Opened terminal on my local machine.

2. Used the SFTP put command to upload the Tasks screenshots to the command_line_for_the_win diractory in the alx-system_engineering-devops form my local machine.

    
    sftp <Host_Sandbox>
  (like: e6b1*****.*****b.alx-cod.online)
   

    Entered my password: (like :bb***9*****)

    
    cd  alx-system_engineering-devops/command_line_for_the_win
    

    Listed my local files to verify the file I wanted to upload.

    
    lls
    
    Uploaded the screenshots

    
    put 0-first_9_tasks.jpg
    

3.Waited for the transfer to complete. Once done, I proceed to push it to the "alx-system_engineering-devops" GitHub repository.


## Switching to SSH for Sandbox Access to push Tasks screenshots to GitHub

1. Added the Tasks screenshots file to the Git repository.

    
    git add .
    

2. Commited the changes.

    
    git commit -m "a"
    

3. Pushed the screenshots to the GitHub repository.

    
    git push
