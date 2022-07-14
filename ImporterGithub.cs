using Newtonsoft.Json;
using System.Collections;
using System.Collections.Generic;
using UnityEngine;


public class Importer : MonoBehaviour
{
    public Root cameraData;
    public TextAsset json;
    public List<List<float>> frameData = new List<List<float>>();
    // Start is called before the first frame update



    public class Frames
    {
        public MatrixWorld matrix_world { get; set; }
    }

    public class MatrixWorld
    {

        // From the converted JSON to C# result that you received on https://json2csharp.com, copy and paste all the public lists here. Example:
        // public List<float> frame_1 { get; set; }
        // public List<float> frame_2 { get; set; }
        // public List<float> frame_3 { get; set; }
        // public List<float> frame_4 { get; set; }
        // public List<float> frame_5 { get; set; }
        // public List<float> frame_6 { get; set; }
        // public List<float> frame_7 { get; set; }
        // public List<float> frame_8 { get; set; }
        // public List<float> frame_9 { get; set; }
        // public List<float> frame_10 { get; set; }
    }

    public class Root
    {
        public string cameraName { get; set; }
        public float frameStart { get; set; }
        public float frameEnd { get; set; }
        public float vfov { get; set; }
        public float hfov { get; set; }
        public Frames frames { get; set; }
    }

    private void Awake()
    {
        //Set the correct frame rate here
        Application.targetFrameRate = 24;
    }
    void Start()
    {
        cameraData = JsonConvert.DeserializeObject<Root>(json.ToString());
        
    }

    // Update is called once per frame
    void Update()
    {
  
        // Change the frame count according to your correct number. In this example, there are 10 frames
        if (Time.frameCount <= 10)
        {
           string loopString = "frame_" + Time.frameCount.ToString();
           if (loopString == cameraData.frames.matrix_world.GetType().GetProperty(loopString).Name)
           {

                List<float> framedata = (List<float>)cameraData.frames.matrix_world.GetType().GetProperty(loopString).GetValue(cameraData.frames.matrix_world, null);
                Camera.main.transform.position = new Vector3(framedata[0], framedata[1], framedata[2]);
                Camera.main.transform.rotation = Quaternion.Euler(framedata[3],framedata[4],framedata[5]);
           }
        }
       


      

    }
}
