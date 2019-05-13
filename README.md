# Bowtie Reimplementation by Python 

------

This is a project README file of CS177H Bioinfomatics by Prof. Jie Zheng , ShanghaiTech University.

### Function implementation

|                          | Raw Bowtie | Raw Bowtie 2 |   Reimplement Version   |
| :----------------------: | :--------: | :----------: | :---------------------: |
| Exact Match (End to End) |     ✔      |      ✔       |            ✔            |
|  Gap match and mismatch  |     ✘      |      ✔       |        ✔(beta *)        |
|   Finish Notification    |     ✘      |      ✘       | ✔(remote server needed) |

* Due to knowledgement limitation , there are some known issue processing gap match and mismatch, thus it will be somehow annoying dealing with gap match, the accuracy is not guaranteed.

### Definition explanation (IMPORTANT FOR UNDERSTANDING)

- Reference DNA series : refers to the DNA series which is comparable longer as an input.

- Compared DNA seriss : refers to the DNA series which is comparable shorter as an input.

  

### Running Environment 

This reimplementation is purely build on Python which provided extendable features and much more possibilities. The following environmental conditions should be satisfied to run the Python-version Bowtie.

- Python 3.7 or later
- Python packages needed ( easily installed by `pip3 install` command)
  - progressbar
  - pandas
  - xlsxwriter

### Usage introduction

To use the reimplement version, the referrence  and compared DNA series information should be stored separately in each FASTA file which contains ONLY ONE series information, if one more series information is contained in one FASTA file, the Reimplement version will ignore  all the series except the first one.

**NOTE** : The input file should contains letters no other than 'A','T','C' and 'G', other letters cannot be processed correctly and may lead to a logical crash of the program, it should be fixed in the following version.

Call the programm using `python3` in your terminal ( be sure a minimum version of 3.7 is installed on your PC )

the calling should be in the following format:

`python3 bowtie2xl.py [path/your reference FASTA file] [path/your compared FASTA file]`

Example:

`python3 bowtie2xl.py reference.fasta compared.fasta`

once given the correct file you should see text like:

```
index processing begins
Progress: 100% |####################################| ElapsedTime:0:00:15 Time:0:00:15
index success!
search begins !
```

The index progress is show simultaneously as a progressbar and ETA, which makes it a lot more easier to allocate time.

which indicates the processing state, and when the comparation is done , the output will be available on both terminal screen and a text file output to the same path as the py file called 'a.txt'. 

One more thing, if you have set the notification function correctly before using , you will get a notification on your mobile phone simultaneously when the output is available, which can dramatically reduced your checking frequency when running something big on Bowtie.

Here shows the output example when enable the screen show

```
Well done !
This is NO.1 alignment answer
ACGTGTCATTAGTGATGTGACGGATCAGTCATGACGATACGATGACTGACTACGGATCAGTCAGCATGACGATAGCAGA
----------------GTG------------------------------------------------------------

This is NO.2 alignment answer
ACGTGTCATTAGTGATGTGACGGATCAGTCATGACGATACGATGACTGACTACGGATCAGTCAGCATGACGATAGCAGA
-----------GTG-----------------------------------------------------------------

This is NO.3 alignment answer
ACGTGTCATTAGTGATGTGACGGATCAGTCATGACGATACGATGACTGACTACGGATCAGTCAGCATGACGATAGCAGA
--GTG--------------------------------------------------------------------------
```

Here shows the output example when enable the Excel generration by command `-r`

### Special feature: Finish Notification

Many bioinformaticians are bothers with aligning sequences which are too big, it will be always time-consuming and complex when dealing with the output answer.

Finish Notification helps when you do not know how much time it will cost to finish the aligning. By using Finish Notification, you will be able to do other research work other than sitting in front of your desk checking it was done or not.

It should be look like this on your smartphone when your work is done

<div align=center><img width="250" height="500" src="/screenshot1.JPEG"/></div>

To use Finish Notification , requirements below should be satisfied:

- A PC with stable network connection.
- An iPhone or iPad running iOS 10.0 or later  (Android Phone has not been tested due to equipment limitation, but it should be theoretically available through FCP Framework)
- A private server ruuning Ubuntu 16.04 LTS  (optional)

The following steps must be done to receive a notification:

1. Download and install **Barks** on AppStore

2. (Optional) For better safety guarantees, it is recommanded to set up your own server side on VPS and the following command should be useful. **NOTE**: Do not try to install the notification service on your mainly-used VPS if you don't understand what the command was doing.

   1. **Docker**

      ```
      docker run -dt --name bark -p 8080:8080 -v `pwd`/bark-data:/data finab/bark-server
      ```

   2. **Docker-Compose**

      ```
      mkdir bark && cd bark
      curl -sL https://git.io/fhAsj > docker-compose.yaml
      docker-compose up -d
      ```

   3.  **Run** `curl http://0.0.0.0:8080/ping` **to test if the service is available on server side**

   4. Type in your VPS **public IP addres** in Barks and edit the very **first line** of the py file

3. If you do not want to bother with setting up server side services, you can use a public notification instead, just get your own **ID** in **Barks** and edit the py file in the very **first line** to enable notification. The ID should be seen like the format like `dgMCtB2A6VtfKjnpcpFfV4`

4. Enjoy

### Special feature: Excel file output

For reference DNA series much too longer, it would be annoying if all the alignment is showed in terminal. Thus you can simply add `-r` command in the very end to diable screen show in the terminal and enable excel output. 

Once the alignment is done, a Excel file with extended name `xlsx` will be generated for further analysis which contains the index  of every matched loacation.

1. Download and install **Barks** from App Store as a notification receiver ( It is necessary ) due to Apple's policy of Notification.

2. (Optional) For stronger safety guarantees, it is recommended to setup an server side software on your own VPS, which can be done simply by a installation command.

   1. For Docker:

       `docker run -dt --name bark -p 8080:8080 -v pwd/bark-data:/data finab/bark-server`

      For Docker Compose

      ```
      mkdir bark && cd bark
      curl -sL https://git.io/fhAsj > docker-compose.yaml
      docker-compose up -d
      ```

   2. Usage

      ```
      curl http://0.0.0.0:8080/ping
      ```

   