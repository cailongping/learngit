# learngit
#This is my first gitdemo

### git怎么合并远程分支

一共就五步：

1、把代码clone到本地仓库

​          git clone https://github.com/573734817pc/shop.git

2、在本地创建dev分支并与远程dev分支对应

​          git checkout -b dev origin/dev

3、切换到master分支

​          git checkout master

4、本地的dev合并到master上（遇到冲突解决完后再次提交）

​          git merge dev

5、推送到远程的master上

​         git push origin master  