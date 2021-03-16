docker build . -t zakuro/zakuro-cache
docker run --rm -it zakuro/zakuro-cache time python demo.py
docker run --rm -it zakuro/zakuro-cache time python demo.py --nocache
