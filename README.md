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
index success !
search begins !
```

which indicates the processing state, and when the comparation is done , the output will be available on both terminal screen and a text file output to the same path as the py file called 'a.txt'. 

One more thing, if you have set the notification function correctly before using , you will get a notification on your mobile phone simultaneously when the output is available, which can dramatically reduced your checking frequency when running something big on Bowtie.

Here shows the output example

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



### Special feature: Finish Notification

Many bioinformaticians are bothers with aligning sequences which are too big, it will be always time-consuming and complex when dealing with the output answer.

Finish Notification helps when you do not know how much time it will cost to finish the aligning. By using Finish Notification, you will be able to do other research work other than sitting in front of your desk checking it was done or not.

It should be look like this on your smartphone when your work is done

<img src="/screenshot1.JPEG" style="zoom:25%" />

To use Finish Notification , requirements below should be satisfied:

- A PC with stable network connection.
- An iPhone or iPad running iOS 10.0 or later  (Android Phone has not been tested due to equipment limitation, but it should be theoretically available through FCP Framework)
- A private server ruuning Ubuntu 16.04 LTS  (optional)

