cd data

#download road data
wget http://kitti.is.tue.mpg.de/kitti/data_road.zip
unzip data_road.zip
rm data_road.zip

#download the vgg pre-trained the data
wget https://s3-us-west-1.amazonaws.com/udacity-selfdrivingcar/vgg.zip
unzip vgg.zip
rm vgg.zip

cd ..

#this package is required in the AWS AMI because it has not been configured, so you need to install it by yourself
pip install tqdm