import java.io.IOException;
import java.util.StringTokenizer;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.Mapper;
import org.apache.hadoop.mapreduce.Reducer;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;

public class GreenCount {

  public static class TokenizerMapper
       	extends Mapper<Object, Text, Text, IntWritable>{

    private final static IntWritable one = new IntWritable(1);
    
    private Text word1 = new Text("Greater than 75%");
	private Text word2 = new Text("Lesser than 75%");
    public void map(Object key, Text value, Context context)
		throws IOException, InterruptedException {
		String valueString = value.toString();
		String[] rowData = valueString.split(",");
		//word1 = "Greater than 75%";
		//word2 = "Greater than 75%";
		double green = Double.parseDouble(rowData[rowData.length - 1]);
		if(green >= 0.75000000000000000)
			context.write(word1, one);
		else
			context.write(word2, one);	
		/*
      StringTokenizer itr = new StringTokenizer(value.toString());
      while (itr.hasMoreTokens()) {
        word.set(itr.nextToken());
        context.write(word, one);
      }
      */
    }
  }

  public static class IntSumReducer
       	extends Reducer<Text,IntWritable,Text,IntWritable> {
       
    private IntWritable result = new IntWritable();

    public void reduce(Text key, Iterable<IntWritable> values,Context context)
    	throws IOException, InterruptedException {
    	
      int sum = 0;
      for (IntWritable val : values) {
        sum += val.get();
      }
      result.set(sum);
      context.write(key, result);
    }
  }

  public static void main(String[] args) throws Exception {
    Configuration conf = new Configuration();
    Job job = Job.getInstance(conf, "green count");
    job.setJarByClass(GreenCount.class);
    job.setMapperClass(TokenizerMapper.class);
    job.setCombinerClass(IntSumReducer.class);
    job.setReducerClass(IntSumReducer.class);
    job.setOutputKeyClass(Text.class);
    job.setOutputValueClass(IntWritable.class);
    FileInputFormat.addInputPath(job, new Path(args[0]));
    FileOutputFormat.setOutputPath(job, new Path(args[1]));
    System.exit(job.waitForCompletion(true) ? 0 : 1);
  }
}
