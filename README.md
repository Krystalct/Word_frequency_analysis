# Word_frequency_analysis
1.统计词频信息并通过引入凝固度和自由度的概念对词进行筛选，最终对筛选结果绘制出词云图；2.输入一组词绘制其在每一章的词频变化折现图
## count_times.py

分块统计该篇文章的词频信息并存储到文件

### input：

* 待处理的文章


### output:
	
* 处理后的结果文件集

## c_stopwords.py
根据统计词频后的文件生成停用词(将)然后存储到文件

###**input:**
* 统计词频后的文件（用来生成停用词的）的存储位置

###**output:**
* 生成的停用词的文件位置


## ResultFile.py
	
`class` ResultFile 的定义文件，该类用来管理有多个子文件的文件目录（主要是一些结果文件）

## WordList.py

`class` WordList 的定义文件，用来管理一个pd.DataFrame()的读写

## c_stopwords.py

生成停用词
### input:

* 用来生成停用词的源文件目录

### output：

* 生成的停用词


## del_stopwords.py
###input:

* 统计词频后的要删除停用词的目标文件
* 停用词文件

###output:

* 去除停用词后的文件

## select_word.py

根据已经计算得到的凝固度和自由度(分左自由度`fr_left`和右自由度`fr_right`) 计算`score`(=`co`\*`fr_left`*`fr_right`)然后 
过滤掉`score`<100的词，并将计算结果`pd.DataFrame(columns=['times','co','fr_left','fr_right'],index='word_segment')`存储到文件

### input:

* 凝固度计算结果的存储位置
* 自由度计算结果的存储位置

### output：
* score的计算结果


## draw_wordcloud.py
绘制经过筛选的词的词云
### input:
* 经过选择的词列表的存储位置
### output:
词云图

## chapters.py
绘制某些词的章回变化折线图
### input：
* 要统计词频的词语列表
* 要统计的词的源文件位置

### output:

* 折线图
