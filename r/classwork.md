classwork
================

-   [Brief R Tutorial](#brief-r-tutorial)
-   [Transformation in ranks](#transformation-in-ranks)

Brief R Tutorial
----------------

``` r
A<-c(1,2,3)
D<-data.frame(alg=c(1,2,3),res=c(12,10,13))

D<-read.table("../res/res.txt")
colnames(D)<-c("alg","inst","k","cost","sec")
boxplot(cost ~ alg, data=D, horizontal=TRUE, las=1)
```

![](classwork_files/figure-markdown_github/basics-1.png)

``` r
plot(D$cost,D$sec,las=1)
```

![](classwork_files/figure-markdown_github/scatterplot-1.png)

``` r
library(dplyr)

D<-mutate(D,alg=factor(alg))
#D<- D %>% mutate(alg=factor(alg))

D$class<-NA
D$class[ grep("A-", D$inst)] <- "Augerat"
D$class[ grep("CMT", D$inst)] <- "CMT"
D$class[ grep("Golden", D$inst)] <- "Golden"

D <- D %>% mutate(inst=gsub(".xml","",inst)) %>% mutate(inst=factor(inst))
```

``` r
save(D,file="results.rda")
load("results.rda")
```

    ## % latex table generated in R 3.2.3 by xtable 1.8-2 package
    ## % Wed Apr  1 10:06:20 2020
    ## \begin{table}[ht]
    ## \centering
    ## \begin{tabular}{rlrrrrrr}
    ##   \hline
    ##  & inst & 3702445 & 4621216 & 5403484 & 5475577 & 5755964 & 6012153 \\ 
    ##   \hline
    ## 1 & A-n32-k05 &   5 &   5 &   5 &   5 &   5 &   5 \\ 
    ##   2 & A-n33-k05 &   5 &   5 &   5 &   6 &   5 &   5 \\ 
    ##   3 & A-n33-k06 &   6 &   6 &   6 &   7 &   7 &   6 \\ 
    ##   4 & A-n34-k05 &   6 &   6 &   5 &   5 &   5 &   5 \\ 
    ##   5 & A-n36-k05 &   5 &   5 &   5 &   5 &   5 &   5 \\ 
    ##   6 & A-n37-k05 &   5 &   5 &   5 &   5 &   6 &   5 \\ 
    ##   7 & A-n37-k06 &   7 &   7 &   6 &   7 &   6 &   7 \\ 
    ##   8 & A-n38-k05 &   6 &   6 &   5 &   6 &   6 &   6 \\ 
    ##   9 & A-n39-k05 &   6 &   5 &   5 &   5 &   5 &   5 \\ 
    ##   10 & A-n39-k06 &   7 &   6 &   6 &   6 &   6 &   6 \\ 
    ##   11 & A-n44-k06 &   7 &   6 &   6 &   7 &   7 &   6 \\ 
    ##   12 & A-n45-k06 &   9 &   7 &   6 &   7 &   7 &   7 \\ 
    ##   13 & A-n45-k07 &   8 &   7 &   7 &   7 &   7 &   7 \\ 
    ##   14 & A-n46-k07 &   8 &   7 &   7 &   7 &   7 &   7 \\ 
    ##   15 & A-n48-k07 &   8 &   7 &   7 &   7 &   7 &   7 \\ 
    ##   16 & A-n53-k07 &   8 &   8 &   7 &   8 &   8 &   7 \\ 
    ##   17 & A-n54-k07 &   8 &   8 &   7 &   8 &   7 &   7 \\ 
    ##   18 & A-n55-k09 &  11 &   9 &   9 &  10 &   9 &   9 \\ 
    ##   19 & A-n60-k09 &  10 &   9 &   9 &   9 &   9 &   9 \\ 
    ##   20 & A-n61-k09 &  11 &  11 &  10 &  11 &  10 &  10 \\ 
    ##   21 & A-n62-k08 &   9 &   8 &   8 &   8 &   8 &   8 \\ 
    ##   22 & A-n63-k09 &  11 &  10 &  10 &  10 &  10 &  10 \\ 
    ##   23 & A-n63-k10 &  11 &  11 &  10 &  11 &  10 &  10 \\ 
    ##   24 & A-n64-k09 &  10 &   9 &   9 &   9 &   9 &  10 \\ 
    ##   25 & A-n65-k09 &  11 &  10 &   9 &  10 &  10 &   9 \\ 
    ##   26 & A-n69-k09 &  11 &  10 &   9 &   9 &   9 &   9 \\ 
    ##   27 & A-n80-k10 &  13 &  10 &  10 &  11 &  10 &  10 \\ 
    ##   28 & CMT01 &   6 &   6 &   5 &   6 &   6 &   5 \\ 
    ##   29 & CMT02 &  12 &  11 &  10 &  11 &  11 &  11 \\ 
    ##   30 & CMT03 &   9 &   8 &   8 &   8 &   8 &   8 \\ 
    ##   31 & CMT04 &  14 &  12 &  12 &  12 &  12 &  12 \\ 
    ##   32 & CMT05 &  21 &  17 &  17 &  17 &  17 &  17 \\ 
    ##   33 & CMT11 &   8 &   8 &   7 &   7 &   7 &   7 \\ 
    ##   34 & CMT12 &  10 &  10 &  10 &  10 &  10 &  10 \\ 
    ##   35 & Golden\_01 &  11 &   9 &   9 &   9 &   9 &   9 \\ 
    ##   36 & Golden\_02 &  12 &  10 &  10 &  10 &  10 &  10 \\ 
    ##   37 & Golden\_03 &  12 &   9 &   9 &   9 &   9 &   9 \\ 
    ##   38 & Golden\_04 &  12 &  10 &  10 &  10 &  10 &  10 \\ 
    ##   39 & Golden\_05 &   6 &   5 &   5 &   5 &   5 &   5 \\ 
    ##   40 & Golden\_06 &   7 &   7 &   7 &   7 &   7 &   7 \\ 
    ##   41 & Golden\_07 &   9 &   9 &   8 &   9 &   8 &   9 \\ 
    ##   42 & Golden\_08 &  13 &  10 &  10 &  10 &  10 &  10 \\ 
    ##   43 & Golden\_09 &  17 &  15 &  14 &  15 &  14 &  14 \\ 
    ##   44 & Golden\_10 &  19 &  16 &  16 &  17 &  16 &  16 \\ 
    ##   45 & Golden\_11 &  22 &  18 &  18 &  18 &  18 &  18 \\ 
    ##   46 & Golden\_12 &  24 &  20 &  19 &  20 &  20 &  19 \\ 
    ##   47 & Golden\_13 &  33 &  28 &  26 &  30 &  28 &  26 \\ 
    ##   48 & Golden\_14 &  36 &  31 &  30 &  32 &  31 &  30 \\ 
    ##   49 & Golden\_15 &  39 &  35 &  33 &  36 &  34 &  34 \\ 
    ##   50 & Golden\_16 &  48 &  39 &  37 &  40 &  39 &  37 \\ 
    ##   51 & Golden\_17 &  27 &  22 &  22 &  23 &  24 &  22 \\ 
    ##   52 & Golden\_18 &  33 &  28 &  27 &  28 &  27 &  29 \\ 
    ##   53 & Golden\_19 &  39 &  34 &  33 &  35 &  33 &  34 \\ 
    ##   54 & Golden\_20 &  46 &  39 &  38 &  40 &  39 &  39 \\ 
    ##    \hline
    ## \end{tabular}
    ## \end{table}

Transformation in ranks
-----------------------

``` r
require(dplyr)
EVAL_LONG <- D %>% group_by(inst) %>% mutate(rank=rank(k,na.last = TRUE)) %>% ungroup()
EVAL_LONG
```

    ## # A tibble: 324 x 7
    ##        alg      inst     k  cost   sec  class  rank
    ##     <fctr>    <fctr> <int> <dbl> <dbl>  <chr> <dbl>
    ##  1 3702445 Golden_20    46  2381 14.40 Golden     6
    ##  2 3702445 Golden_19    39  1783  9.31 Golden     6
    ##  3 3702445 Golden_18    33  1309  5.55 Golden     6
    ##  4 3702445 Golden_17    27   965  3.15 Golden     6
    ##  5 3702445 Golden_16    48  2291 20.38 Golden     6
    ##  6 3702445 Golden_15    39  1781 11.44 Golden     6
    ##  7 3702445 Golden_14    36  1500  6.39 Golden     6
    ##  8 3702445 Golden_13    33  1191  3.41 Golden     6
    ##  9 3702445 Golden_12    24  1455 21.33 Golden     6
    ## 10 3702445 Golden_11    22  1178 12.01 Golden     6
    ## # ... with 314 more rows

``` r
# tbl_df(EVAL_LONG) # from tibble to data frame to show all rows 
```

We can order the levels of the `alg` factor as follows:

``` r
require(ggplot2)
p <- ggplot(EVAL_LONG,aes(x=reorder(alg, rank, median), y=rank)) # we start the plot saying which data and aestetics to use
p <- p + geom_boxplot(aes(fill=alg),width=0.8,stat = "boxplot",
                  position = position_dodge(width = 0),
                  colour = I("#3366FF"),outlier.colour = I("#3366FF"))
p <- p + guides(fill=FALSE) # remove the fill legend
p <- p + geom_jitter(size=1.2,position = position_jitter(height=0,width=0.4))
p <- p + coord_cartesian(ylim=c(1,nlevels(EVAL_LONG$alg))) 
p <- p + scale_y_continuous(breaks=seq(1, nlevels(EVAL_LONG$alg), 1))
# p <- p + scale_y_continuous(limits=c(1,nlevels(DATA$alg)))
p <- p + labs(x="user")
p <- p + coord_flip() # show the plot horizontally
#p <- p + scale_fill_manual(name = "alg", values = myColors)
#p <- p + facet_grid(class~.)
p <- p + facet_grid(.~class) # faceting
print(p)
```

<img src="classwork_files/figure-markdown_github/bwrankhard-1.png" style="display: block; margin: auto;" />

``` r
require(dplyr)
EVAL_LONG <- EVAL_LONG %>% mutate(alg=factor(alg,levels=levels(reorder(EVAL_LONG$alg, EVAL_LONG$rank, median))))
```

``` r
# we prepare the colors
library(RColorBrewer)
colfun <- colorRampPalette(brewer.pal(12, "Paired"))
myColors <- colfun(nlevels(D$alg)) # we keep out the entries from the previous year
# myColors <- c(myColors,rep("#FFFFFF",9)) # white for the entries from the previous year
names(myColors)<-levels(D$alg)
```
