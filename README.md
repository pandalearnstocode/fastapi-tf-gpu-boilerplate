# Fast API Tensorflow GPU boilerplate

To run this, one has to have a GPU enabled system with Nvidia drive and docker installed. Here we are not covering this part. It is just to give a quick start setup which will increase development velocity.


## Build and check things in local

```
docker build -t gpu_engine .  
docker run --gpus all -d -p 80:80 gpu_engine 
```

__Note:__ The above docker run command is different than the normal docker run. `--gpu all` tag ensures that we are using a Nvidia docker. Here we have taken tensorflow gpu image as the base image. Also we have used the other required file to run Fast API in the image.

## Additional note:

I have check this image works with any NC series VM and azure container instances. This is a good way to run a mid-size workload. Specially this is useful if you have a long running mid sized workload which does not require scaling. In case scaling is must go for a AKS and KEDA base approach with GPU based cluster. Another serverless approach can be to use Azure Function/ Durable Functions with KEDA and AKS using GPU cluster. 