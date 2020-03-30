
library("dplyr")
library("ggplot2")



#load the data and give names to fields
D2019 <- read.table("../res/res.txt",fill=TRUE)
colnames(D2019)<- c("alg","instance","routes","eval","time")
D2018 <- read.table("./res-2018.txt",fill=TRUE)
colnames(D2018)<- c("alg","instance","routes","eval","time") #,"time")
D2018 <- mutate(D2018,alg=factor(alg))
levels(D2018$alg)<-paste("x-2018",letters[1:nlevels(D2018$alg)],sep="-")
D2019<-rbind(D2019,D2018)

D2019$class<-NA
D2019$class[ grep("A-", D2019$instance)] <- "Augerat"
D2019$class[ grep("CMT", D2019$instance)] <- "CMT"
D2019$class[ grep("Golden", D2019$instance)] <- "Golden"

D2019 <- D2019 %>% mutate(alg=gsub("3702445","Savings",alg))
D2019 <- mutate(D2019,
          alg=factor(alg)
          )

D2019 <- D2019 %>% mutate(instance=gsub(".xml","",instance)) %>% mutate(instance=factor(instance))
#D<-rbind(D,data.frame(alg="GLS",instance=bo$V1,hard=bo$V2,soft=bo$V3,eval=0,time=120))


## ----echo=TRUE-----------------------------------------------------------
DATA <- D2019
save(DATA,file="results.rda")

## ----echo=FALSE, message=FALSE, warning=FALSE, results='hide'------------
## Let's make the ranks of the violated clauses
#load("results.rda")
#T1 <- split(DATA["cost"], DATA["instance"])
#T2 <- lapply(T1, rank, na.last = "keep")
#T3 <- unsplit(T2, DATA["instance"])
#DATA$rank <- T3

## ----loaddata, echo=TRUE, message=FALSE, warning=FALSE-------------------
load("results.rda")

## ----tables, echo=TRUE, message=FALSE, warning=FALSE---------------------
require(tidyr)
spread(select(DATA,instance,alg,routes),alg,routes)
spread(select(DATA,instance,alg,eval),alg,eval)
spread(select(DATA,instance,alg,time),alg,time)

## ---- echo=TRUE, eval=FALSE, message=FALSE, warning=FALSE----------------
## require(reshape2)
## dcast(DATA,instance~alg,value.var="hard")
## dcast(DATA,instance~alg,value.var="soft")
## dcast(DATA,instance~alg,value.var="time")

## ----makehardrank, echo=TRUE, message=FALSE, warning=FALSE---------------
#DATA <- DATA %>% filter(instance != "co-100")
# EVAL <- spread(select(DATA,instance,alg,eval),alg,eval)
#rownames(COST) <- levels(COST$instance)
#(COST_RANK <- apply(COST[,2:8],1,rank,na.last=TRUE))
# EVAL_LONG <- gather(EVAL,"alg","eval",2:8)
require(dplyr)
EVAL_LONG <- DATA %>% group_by(instance) %>% mutate(rank=rank(eval,na.last = TRUE)) %>% ungroup()
EVAL_LONG <- EVAL_LONG %>% mutate(alg=factor(alg,levels=levels(reorder(EVAL_LONG$alg, EVAL_LONG$rank, median))))

## ----colorsetting, echo=TRUE, message=FALSE, warning=FALSE---------------
library(ggplot2)
# we prepare the colors
library(RColorBrewer)
colfun <- colorRampPalette(brewer.pal(12, "Paired"))
myColors <- colfun(nlevels(DATA$alg)) # we keep out the entries from the previous year
# myColors <- c(myColors,rep("#FFFFFF",9)) # white for the entries from the previous year
names(myColors)<-levels(DATA$alg)

## ----bwrankhard, echo=TRUE, fig.align='center', fig.width=13, fig.height=7, warning=FALSE, message=FALSE----
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
# p <- p + facet_grid(.~class) # faceting
p <- p + coord_flip() # show the plot horizontally
p <- p + scale_fill_manual(name = "alg",values = myColors)
p <- p + facet_grid(EVAL_LONG$class~.)
print(p)

