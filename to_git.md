togit
================

GitHub Documents
----------------

This is an R Markdown format used for publishing markdown documents to GitHub. When you click the **Knit** button all R code chunks are run and a markdown file (.md) suitable for publishing to GitHub is generated.

Including Code
--------------

You can include R code in the document as follows:

``` r
summary(cars)
```

    ##      speed           dist       
    ##  Min.   : 4.0   Min.   :  2.00  
    ##  1st Qu.:12.0   1st Qu.: 26.00  
    ##  Median :15.0   Median : 36.00  
    ##  Mean   :15.4   Mean   : 42.98  
    ##  3rd Qu.:19.0   3rd Qu.: 56.00  
    ##  Max.   :25.0   Max.   :120.00

Including Plots
---------------

You can also embed plots, for example:

![](to_git_files/figure-markdown_github/pressure-1.png)

Note that the `echo = FALSE` parameter was added to the code chunk to prevent printing of the R code that generated the plot.

Analysis of results
-------------------

This page shows how to carry out an analysis of results in R. The scenario of analysis in Assignment 1 is single pass heuristics tested with a single run on multiple instances, each run with a time limit of 60 seconds. Hence, the analysis must take into account a bivariate performance measure. There are three classes of instances: Augerat, CMT and Golden. Among the instances of type CMT only the instances CMT1, CMT2, CMT3, CMT12, CMT11, CMT4 and CMT5 have been included. The others include maximum distance and service time constraints that we do not handle. Hence they were discarded.

The results are collected in a file <a href="./res.txt">res.txt</a>. The results are collected in a file <a href="./res.txt">res.txt</a>. Each row of the file contains the userID, the name of the instance, the number of routes, the total cost of the solution and the running time when the program terminated. The userID Saving is a classic algorithm for CVRP, the saving heuristic. Each row of the file contains the userID, the name of the instance, the number of routes, the total cost of the solution and the running time when the program terminated. The userID Saving is a classic algorithm for CVRP, the savings heuristic.

Data preprocessing
------------------

We load the results in R and ensure that the fields alg and instance are trated as factors.

\`\`\`r \#load the data and give names to fields D2019 &lt;- read.table("../res/res.txt",fill=TRUE) colnames(D2019)&lt;- c("alg","instance","routes","eval","time") D2018 &lt;- read.table("./res-2018.txt",fill=TRUE) colnames(D2018)&lt;- c("alg","instance","routes","eval","time") \#,"time") D2018 &lt;- mutate(D2018,alg=factor(alg)) levels(D2018$alg)&lt;-paste("x-2018",letters\[1:nlevels(D2018$alg)\],sep="-") D2019&lt;-rbind(D2019,D2018)

D2019*c**l**a**s**s* &lt; −*N**A**D*2019class\[ grep("A-", D2019$instance)\] &lt;- "Augerat" D2019$class\[ grep("CMT", D2019$instance)\] &lt;- "CMT" D2019$class\[ grep("Golden", D2019$instance)\] &lt;- "Golden"

D2019 &lt;- D2019 %&gt;% mutate(alg=gsub("3702445","Savings",alg)) D2019 &lt;- mutate(D2019, alg=factor(alg) )

D2019 &lt;- D2019 %&gt;% mutate(instance=gsub(".xml","",instance)) %&gt;% mutate(instance=factor(instance)) \#D&lt;-rbind(D,data.frame(alg="GLS",instance=bo*V*1, *h**a**r**d* = *b**o*V2,soft=bo$V3,eval=0,time=120))

``` }
```

    Error: attempt to use zero-length variable name
