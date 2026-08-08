# 面向有机合成课题组的傻瓜化核磁计算平台

### 前言

笔者目前是一位处于天然产物全合成课题组的在读博士生。在本科阶段，本科的导师时常与笔者畅想“未来的有机化学”，这一宏大愿景下的一项命题即为“计算辅助的有机化合物的结构解析”，在那时我们便设想搭建一个面向有机合成课题组的实用化的计算化学辅助的有机化合物结构解析平台。然而，在各种不可抗力的影响下，这一计划一拖再拖，尽管积累了很多素材、知识和经验，但一直到本科毕业，笔者也未能去完成这一实践。幸运的是，在研究生阶段，恰逢课题组遇到了目标分子原始结构鉴定有误的难题，笔者提出可以通过核磁计算的方式重新解析天然产物结构，最终揭示出若干个不同寻常的结构突变并得到了合成化学的印证（[*J. Am. Chem. Soc.* **2025**, *147*, 33136.](https://doi.org/10.1021/jacs.5c11010)）。通过此次偶然的实践，笔者所处的一个传统的天然产物全合成课题组与核磁计算的工具建立起了牢靠的信任关系。事实上，在日常的合成研究中，每一步反应所得的高级中间体，其结构之复杂与精巧并不亚于天然产物本身，而计算亦从不区分人工与天然，因此这一实用的工具有望用于辅助课题组内对于合成中间体的日常结构鉴定。笔者为此重新拾起本科时期的设想，花费了几个月的构思、学习与尝试，充分考虑一个忙碌的有机合成课题组的日常需求，选取了若干实用的核磁计算流程，通过将自编的批处理脚本和现有程序相结合的方式，为组内初步搭建了一套傻瓜化核磁计算平台，实现了从输入记录化合物结构的.xyz文件到输出易于处理的数据文件的一键化计算，现将这一初步的成果和相应的使用经验与大家分享，欢迎各位批评指正。



### 1. 简介

#### 1.1 **有机合成化学家为什么需要核磁计算？**

在各种有机化学或仪器分析的教材中，我们学习了很多实用的现代技术用于有机化合物的结构表征与鉴定，如红外、拉曼、紫外、核磁、质谱、X-射线单晶衍射等。在实践中，面临一个新的有机化合物的结构鉴定，核磁往往成为有机化学家的首选。抛开技术发展和测试成本问题，笔者认为核磁成为首选的一个重要原因是其可预见性更强，即在有机化学家的知识体系下，一个给定的有机物结构对应的特征核磁信号可以在人脑的计算量下获得直观的预测，正是一系列预测值与实验值相吻合的自洽加强了有机化学家对结构研判无误的信心。因此，有机化学家对核磁谱图的解析能力的强弱直接取决于其预测水平的高低，而核磁计算本身就是在对核磁信号进行预测。值得注意的是，人脑面临例如长程耦合的强弱、同类质子的化学位移的相对大小等更精细的结构信息的预测往往束手无策，而核磁计算总能给出答案。核磁计算能辅助有机化学家从更多的角度去发掘预测值与实验值相吻合的自洽，无疑会提高其对有机物结构的解析能力。

#### 1.2 有机合成化学家需要什么精度的核磁计算？



#### 1.3 计算模块功能简介

##### 1.3.1 DP4+/MM-DP4+/dJ-DP4/ML-J-DP4



##### 1.3.2 ANN-PRA



##### 1.3.3 autohnmr



##### 1.3.4 STS



### 2. 系统配置

笔者所在的有机合成课题组所接触的计算以量子化学计算为主，研究体系一般均为不超过150个原子的常规有机分子（元素组成基本为C、H、O、N，成键上无特殊的电子结构）。笔者使用的这台服务器是课题组于2023年暑期购置的，其配置基本上照搬了当时卢天老师博文中推荐的入门配置（[http://sobereva.com/444](http://sobereva.com/444)，最新版博文中已不再有这套推荐配置），当时的花费为6900元。

CPU：2 × Intel Xeon E5-2696 v3 （单颗18核36线程，2.3 GHz，无集显）

散热器：2 × 利民AS120

主板：超微X10DRL-I（C612芯片组，集显）

机械硬盘：希捷（银河企业版，4 TB，256 MB，7200 rpm，SATA3）

固态硬盘：三星PM981α（1 TB）

内存：8 × 三星/镁光DDR4-2400（ECC，REG，16 GB）

电源：台达（650 W）

机箱：长城磐龙PL-16



### **3. 依赖程序**

操作系统：Rocky Linux 9.7

Gaussian 16 A.0.3（安装见[http://sobereva.com/439](http://sobereva.com/439)）

orca 6.1.1（安装见[http://sobereva.com/451](http://sobereva.com/451)）

xtb 6.7.1（安装见[http://sobereva.com/421](http://sobereva.com/421)）

open babel 3.1.1（安装：打开终端，运行`sudo yum install openbabel`)

CREST 3.0.2（安装见[https://crest-lab.github.io/crest-docs/page/installation/install_basic.html](https://crest-lab.github.io/crest-docs/page/installation/install_basic.html)）

CENSO 1.2.0（安装见[https://github.com/grimme-lab/CENSO/tree/v.1.2.0](https://github.com/grimme-lab/CENSO/tree/v.1.2.0)）

ANMR（安装见[https://github.com/grimme-lab/enso/releases/tag/v.2.0.2](https://github.com/grimme-lab/enso/releases/tag/v.2.0.2)）

molclus 1.14（安装见[http://www.keinsci.com/research/molclus.html](http://www.keinsci.com/research/molclus.html)）

Multiwfn 3.8 (2026.4.10)（安装见[http://sobereva.com/multiwfn/](http://sobereva.com/multiwfn/)）

Python 3.9.25

ssmtp（安装：打开终端，运行`sudo yum install ssmtp`；用于发送提醒邮件，配置见后文）

其中CREST、CENSO、ANMR、molclus和Multiwfn需加入环境变量。



### **4. 计算流程**

**[输入文件]** 计算模块目录下的所有.xyz文件，其记录了化合物结构信息。

**[读取用户信息]** 弹出窗口要求用户选择输出文件压缩包的位置，指定输出文件压缩包名称和用于接收提醒邮件的电子邮箱地址。

**[溶剂选择]** 仅限DP4+、MM-DP4+和STS，前两者通过弹出窗口要求用户选择溶剂，后者通过命令行要求用户选择溶剂。

**[并行任务数选择]** 命令行要求用户选择并行任务数。

为提高计算效率，在部分耗时的计算环节中，计算模块将根据用户指定的并行任务数对体系进行均分，例如用户指定并行任务数为3，体系当前有50个代表不同构象的初始结构有待几何优化，其在计算过程中将被分为任务数分别为17/17/16的三组平行进行几何优化。

**[构象生成]** 利用CREST程序根据输入XXX.xyz文件生成一批代表不同构象的初始结构，结果存于XXX_search文件夹。

**[构象筛选]** 利用CENSO程序调用orca、xtb等程序对上述一批初始结构进行筛选，结果存于XXX_screening文件夹。

**[几何优化]** 利用molclus程序调用Gaussian、openbabel等程序对经上述筛选后的一批结构进行几何优化，结果存于XXX_batch/opt文件夹。

**[核磁计算]** 利用Gaussian基于上述几何优化后的一批结构进行核磁计算，结果存于XXX_batch/nmr文件夹。

**[数据提取]** 根据后续数据处理的需要提取构象平均后的磁屏蔽张量、耦合常数矩阵等数据，结果存于XXX_result文件夹。

ML-J-DP4不支持手动处理数据，无数据提取过程。

autohnmr的构象筛选、几何优化、核磁计算过程均由CENSO程序完成，数据提取由ANMR程序完成，结果一并存于XXX_screening文件夹。

**[输出文件打包和邮件提醒]** 计算完成后将所有输出文件打包为指定名称的.zip文件移动至用户指定的位置，并发送电子邮件提醒用户计算完成以及计算耗时。



### **5. 计算模块本地化设置**

**[第一步]** 进入用户文件夹目录，进入隐藏文件夹.censo_assets，打开文件censo_orca_editable.dat，该文件用于控制CENSO调用orca时的默认关键词，修改其内容为：

```
! miniprint nopop noautostart
%MaxCore 2500
```

**[第二步]** 进入用户文件夹目录，创建隐藏文本文件.anmrrc，该文件用于控制ANMR处理数据的默认选项，写入内容：

```
7 XH acid atoms
ENSO qm= ORCA mf= 400 lw= 1.0  J= on S= on
TMS[chcl3] revtpss[cpcm]/cc-pVTZ//b3lyp-3c[cpcm]
1  31.50    0.0    1
```

**[第三步]** 进入安装CENSO程序的文件夹，进入censo_qm文件夹，打开脚本cfg.py，程序识别的理论方法记录于该文件中，找到第192行，行末换行写入如下内容以添加泛函mPW1PW91和ωB97M-V（注意缩进需严格一致）：

```
		"mPW1PW91": {
			"tm": None,
			"orca": "\n%method\nmethod dft\nexchange gga_x_mpw91\ncorrelation gga_c_pw91\nend",
			"disp": "novdw",
			"part": ["func0", "func", "func3", "func_j", "func_s"],
			"type": "global_hybrid",
		},
		"wb97m-v": {
			"tm": None,
			"orca": "wb97m-v",
			"disp": "included",
			"part": ["func0", "func", "func3", "func_j", "func_s"],
			"type": "rsh_hybrid",
		},
```

**[第四步]** 进入安装CENSO程序的文件夹，进入censo_qm文件夹，打开脚本orca_job.py，找到第249行，替换为如下内容以更正B3LYP-3c方法中的色散校正项（注意缩进需严格一致）：

```
				orcainput["disp"] = ["! d3bj ABC"]
```

**[第五步]** 每个文件夹对应相应的计算模块，与文件夹同名的脚本用于执行整个计算流程，其中以下内容需根据本地计算资源修改：

```
mem_G=24
mem_O=2500
nprocs=12
......
  read -r -p "Choose the Maxthreads (1/2/3):" maxthreads
  if [ "$maxthreads" != 1 ] && [ "$maxthreads" != 2 ] && [ "$maxthreads" != 3 ]
```

此处，mem_G为Gaussian计算任务分配总内存数，单位为GB（autohnmr不涉及Gaussian计算，故无该选项）；mem_O为orca计算任务<u>单核</u>分配内存数，单位为MB；nprocs为Gaussian或orca计算任务分配CPU核数；maxthreads为并行的Gaussian或orca计算任务数。笔者所用的服务器CPU核数为36，每个Gaussian或orca计算任务占12核，用户可指定同时运行1/2/3组任务，对应占用的核数即为12/24/36。若在一台72核服务器上，每个任务占18核，用户可指定同时运行1/2/3/4组任务，则相应代码应修改为：

```
nprocs=18
......
  read -r -p "Choose the Maxthreads (1/2/3/4):" maxthreads
  if [ "$maxthreads" != 1 ] && [ "$maxthreads" != 2 ] && [ "$maxthreads" != 3 ] && [ "$maxthreads" != 4 ]
```

**[第六步]** 每个计算模块中的askinfo.py脚本用于读取用户指定的输出压缩文件的位置和名称以及用于接收提醒邮件的电子邮箱地址，其中第5行需进行修改：

```
dirname = fd.askdirectory(initialdir = "/home/dinglab/calculation/temp",title = "Select the Output Directory")
```

此处，initialdir定义了脚本运行时弹出的默认目录，应修改为方便用户指定位置的目录。

为实现计算结束后的邮件提醒功能，需配置ssmtp程序指定发信邮箱，打开终端，运行如下指令以利用vim编辑器打开ssmtp.conf文件：

```
sudo su
vim /etc/ssmtp/ssmtp.conf
```

于文件末写入如下内容：

```
UseTLS=Yes
root=发信电子邮箱地址
mailhub=发送邮件服务器:端口号
AuthUser=发信电子邮箱地址
AuthPass=授权码
```

此处，例如对于QQ邮箱，mailhub和AuthPass的获取见https://wx.mail.qq.com/list/readtemplate?name=app_intro.html#/agreement/authorizationCode。

**[第七步]** 每个计算模块中的censorc\_XXX文件用于配置CENSO程序，其中以下内容需进行修改：

```
ORCA: /home/dinglab/software/orca_6.1.1
......
GFN-xTB: /home/dinglab/software/xtb_6.7.1/xtb_dist/bin/xtb
CREST: /home/dinglab/software/crest_3.0.2/crest
```

此处分别指定了ORCA、xtb、CREST程序的目录，应根据本机实际情况修改。

**[第八步]** DP4plus、ANN_PRA_15、STS三个计算模块中的NMR计算输入文件由Multiwfn批量创建，首先进入安装Multiwfn程序的文件夹，创建文本文件gjf_selection.txt，写入内容：

```
100
2
10

0
q
```

再进入相应的计算模块文件夹中，打开nmr_calc.sh脚本，其中以下内容需进行修改：

```
  Multiwfn "$inf" < ~/software/Multiwfn_2026.4.10_bin_Linux/gjf_selection.txt > /dev/null
```

此处gjf_selection.txt的目录应根据本机实际情况修改。



### **6.** **算例演示以及数据处理**



### **7.** **课题组公用运作模式示例**



###  **结语**

