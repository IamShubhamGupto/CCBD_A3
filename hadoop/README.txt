su - hduser
start-all.sh
jps
stop-all.sh

//delete previous output/Input
hadoop fs -rm -r -skipTrash hdfs://localhost:54310/user/hduser/Output
hadoop fs -rm -r -skipTrash hdfs://localhost:54310/Input/<Enter file name>

cd /home/hduser/Desktop/GreenCountF/

javac -classpath /usr/local/hadoop/share/hadoop/common/hadoop-common-2.7.2.jar:/usr/local/hadoop/share/hadoop/mapreduce/hadoop-mapreduce-client-core-2.7.2.jar:/usr/local/hadoop/share/hadoop/common/lib/commons-cli-1.2.jar -d /home/hduser/Desktop/GreenCountF *.java

Move manually all the .class files that are generated in /home/hduser/Desktop/GreenCountF/ to a new folder, say GreenCountC => /home/hduser/Desktop/GreenCountF/GreenCountC

cd /home/hduser/Desktop/GreenCountF/

jar -cvf GreenCountJ.jar -C /home/hduser/Desktop/GreenCountF/GreenCountC .

hadoop fs -put -f /home/hduser/Desktop/GreenCountF/information_183.csv /Input/

cd /usr/local/hadoop

bin/hadoop jar /home/hduser/Desktop/GreenCountF/GreenCountJ.jar GreenCount /Input Output

Navigate to "http://localhost:50070" on your web browser
Click on the Utilities tab (top right) => Browse the file system
Click on user => hduser => Output => part-r-00000 => Download
The downloaded file contains the required output
