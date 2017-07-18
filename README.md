# CUPAP
It is framework to correlate android permission with methods used in android applications.</br>

It takes Apk file as input and decompile it to permission it has requested and method associated with it.</br>
By doing so we will get to know unnecessary permissions and</br> dead code (code which won't run because of not granting the permission).</br>
Both of this indicates bad behavior of an application. On further note framework tries to understand what exactly application wants to do with permission it has requested.</br>Motivation to this project is because from android M we can actually turn on and off the permissions </br>This framework will be usefull in knowing which permission to turn on and off.</br>But unfortunately it takes pscout(works only upto API 22 i.e Android 5.1) output for this mapping.</br> So further modification can be done is to work on pscout so that this tool will be more usefull.</br>
This tool can still usefull for higher version but it will no longer track newer methods and</br> permissions(added after Android M).


# Installation

• Install smalisca tool from https://github.com/dorneanu/smalisca (prerequisite).</br>
• Execute command ’cd CUPAP’ .</br>
• On successful execution, run ’python getfile.py.</br>
• Input Apk file to be analyzed (O/P path will be displayed on terminal)


