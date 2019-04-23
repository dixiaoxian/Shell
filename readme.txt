创建新的存储库
echo "# Java-MXObject" >> README.md
git init
git add README.md
git commit -m "first commit"
git remote add origin https://github.com/dixiaoxian/Java-MXObject.git
git push -u origin master

从命令行推送
git remote add origin https://github.com/dixiaoxian/Java-MXObject.git
git push -u origin master


版本：2019年4月4日
ip_id文件
	ip_id.sh:用于测试ping信息
	route.sh + linux命令:如（route.sh "route -n | grep UG"）
Maxwell脚本
	maxwell的启动脚本，防止maxwell挂掉（类似于k8s的效果）
webReturn文件
	获得网页的返回值（可用于检测网页在线信息）
时间：2019年4月4日10:22:10

