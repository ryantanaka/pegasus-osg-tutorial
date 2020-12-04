# Example Workflow: Steps to Run

1. ssh into log-in node
```
ssh <username>@login04.osgconnect.net
# e.g. "ssh ryantanaka@login04.osgconnect.net"
```

2. setup Pegasus path
```
export PATH=/public/ryantanaka/pegasus-5.0.0dev/bin:$PATH
```

3. ensure path set correctly
```
which pegasus-version
```
4. setup Pegasus python path
```
export PYTHONPATH=$(pegasus-config --python)
```

5. get workflow
```
git clone https://github.com/ryantanaka/pegasus-osg-tutorial.git
```

6. go to pegasus-workflow directory
```
cd pegasus-osg-tutorial/pegasus-workflow
```

7. run 
```
./workflow.py
```

## Setting Up Latest Pegasus 

```
wget https://download.pegasus.isi.edu/pegasus/5.0.0dev/pegasus-binary-5.0.0dev-x86_64_rhel_7.tar.gz 
tar -xzvf pegasus-binary-5.0.0dev-x86_64_rhel_7.tar.gz 
cd pegasus-5.0.0dev/bin 
export PATH=$(pwd):$PATH 
export PYTHONPATH=$(pegasus-config --python)
```
