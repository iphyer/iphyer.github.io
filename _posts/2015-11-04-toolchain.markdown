---
layout: post
title: "论文工具链总结"
date: 2015-11-04 00:15
comments: true
categories: 科研
---

# 起因

终于昨天晚上把我的论文初稿写好，拖延症很严重。今天晚上正好把自己拉下来没有总结的东西都总结下，前面几个都是游记这种，这个会回到老本行的科研工具上。

分成两个部分，第一部分如何在服务器上快速的做不同参数的计算；第二个部分如何绘制流场线。

<!--more-->

# 快速参数计算

先说下需求，其实很简单就是如何在模拟计算的使用不同的参数，比如调节下作用势的大小，或者两个粒子的间距这个一般来说你是知道参数多少的。

我使用C语言完成模拟，最重要的是这么一个宏定义:

```c

#define beadsdistance 6// distance between Beads 1 and Beads 2 the centre of the ball

```

然后一个节点只有16个CPU,所以我的一组参数是计算8个RUN，然后做统计，

上bash脚本:

```bash

#!/bin/sh
date="20151028-1"
templatesource="HF-p-d.c"
prefix="HF-p-d"
preprog="HFpd"

mkdir ../run/${date}

for i in $( seq 0 1 )
do
    prog=$preprog${i}
    source=$prefix${i}".c"
    oldline="#define beadsdistance 6// distance between Beads 1 and Beads 2 the centre of the ball"
    line="#define beadsdistance "${i}

    cd ~/source/    
    cp ${templatesource} ./${source}
    sed -i "s@$oldline@$line@" ./${source}
    
    gcc -O2 ${source} -o ${prog} -lm
    mkdir ../run/${date}/dist${i}
    cp ${prog} ../run/${date}/dist${i}
    cd ../run/${date}/dist${i}
    for j in $( seq 1 8 )
    do
        mkdir ~/run/${date}/dist${i}/no${j}
        cd ~/run/${date}/dist${i}/no${j}
        cp ~/run/${date}/dist${i}/${prog} . 
        ./${prog}>record  & 
        sleep 5
        echo "Done${j}"
    done
echo "Done distance ${i}"

done


```

程序的核心就是使用`sed`来替换改变参数的那句宏定义。

当然你可能需要根据自己的需求修改。

# 绘制流场线(如何从MATLAB的figure中得到曲线信息)

其实目标就是绘制需要的流场线，但是我能够使用原始信息就是一些流场的每个点的流向信息，也就是从一个矢量图得到一组连续的流场线信息。

首先这个问题从数学上是可解的，以为——每一个点的流场方向其实代表了流场线的切线方向，所以如果你能够定下起始点(一般选择系统边界代表了流入系统或者流出系统)，那么其实就是解这样一个方程$ \frac{ds}{dt} $ = $ \vec v(x,y) $,这个公式很容易通过龙格库塔这些方法解出$s(x,y)$。当然这个是原理分析，如果你能够使用MATLAB就会发现MATLAB可以提供`streamline`这个函数帮助你很容易的画出流场线。

上代码主代码`chanel.m`

```matlab

clear;
figure
M = dlmread('XXX/Wholevelcoity.txt', '\t');
N = dlmread('XXX/Provelcoity.txt', '\t');

x=N(:,2);
y=N(:,3);
u=N(:,4);
v=N(:,5);

quiver(x,y,15*u,15*v)
daspect([1 1 1]);


%系统参数
Lx = 62;
Ly = 20;

XX = M(:,2);
XX = changeshape(XX,Lx,Ly);

YY = M(:,3);
YY = changeshape(YY,Lx,Ly);

UU = M(:,4);
UU =changeshape(UU,Lx,Ly);

VV = M(:,5);
VV = changeshape(VV,Lx,Ly);

starty=4 : 2 :20;
startx = ones(size(starty));
startx = startx+20 ;

streamline(XX,YY,UU,VV,startx,starty)

ax = get(gcf,'children'); % get all subplots
XALL=[];YALL=[];
for iax = 1:length(ax)
    child = get(ax(iax),'children'); % for each subplot, get all lines
    for ichild = 1 : length(child)
        XALL{end+1} = get(child(ichild),'xdata');
     YALL{end+1} = get(child(ichild),'ydata');
    end
end

for j = 1: length(XALL)-1
    X1=transpose(XALL{1,j});
    Y1=transpose(YALL{1,j});
    figure
    plot(X1,Y1);
    filenm = ['Line'    num2str(j)  '.txt' ];
    fid=fopen(filenm,'w+');
    fprintf(fid, '%f \t %f \n', [X1 Y1]');
    fclose(fid);

end

```

辅助代码`changeshape.m`,主要对于原始数据格式做转置和重新排列以适合MATLAB对于数据格式的要求。

```matlab

function [out] = changeshape(in,Lx,Ly)

XXnew=reshape(in,Lx,Ly);
out = transpose(XXnew);

```
说明

首先是我的输入文件存在一个是不是舍去边界值的区别，所以一个是`Wholevelcoity.txt`和`Provelcoity.txt`，当然每一个都是如下的格式：


```
x   y   vx  vy

```

然后剩下的循环就是从得到的这个流场线中获得自己需要的曲线值，值得强调的是这里非常容易出错，因为你需要不断在MATLAB内部查看数据的存储格式和输出的时候的输出格式，因为MATLAB很有可能使用了错误的存储格式。

然后把导出的结果在gnuplot中画出来。

放一张结果图吧,这个是用Tikz做的组合:


![tu1](/images/toolchian/m9.png)

代码如下:

```latex


\documentclass[tikz]{standalone}
\usetikzlibrary{positioning}
\usepackage{lmodern}
\newcommand{\tikzmark}[2]{\tikz[remember picture, baseline] \node[inner sep=0pt, outer sep=0pt, anchor=base] (#1) {#2};}

\newcommand{\ZuiDa}{\fontsize{100pt}{0.5pt}}

\begin{document}

\begin{tikzpicture}[remember picture]
\node (A) at(-40,0) {
{\includegraphics{B2portB.eps}}
};

\draw (-78.5,25.0) node { \ZuiDa \textbf{(\emph{a})}};


\node[right=of A] (B) at (0,0){
{\includegraphics{B2vector.eps}}
};

\draw (-1.5,25) node { \ZuiDa \textbf{(\emph{b})}};

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%B3
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\node (C) at(0,-60) {
{\includegraphics{B3portB.eps}}
};

\draw (-78.5,-40.0) node { \ZuiDa \textbf{(\emph{c})}};


\node[right=of C] (D) at (-80,-118){
{\includegraphics{B3vector.eps}}
};
\draw (-78.5,-100) node { \ZuiDa \textbf{(\emph{d})}};


%node[right=of B] (C) at (-2.641,-2.15){
%{\includegraphics[width=.5\textwidth]{system5.pdf}}
%};
\end{tikzpicture}
\end{document}

```

核心要点就是把图放到`node`结构里面，调节`node`的位置。
