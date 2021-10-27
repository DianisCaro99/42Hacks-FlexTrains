# 42Hacks-FlexTrains

This project provides a novel approach to enhance schedule performance and reduce waiting time for passengers. We use data mining techniques to fetch data from several data sources as NYC uber data and taxi data, open street map, and real-time traffic information. 

Then we utilize a multilayer perceptron model to predict the occupation for every station for every hour. Then, we use another multilayer perceptron to predict the final destination for every passenger based on his initial location and departure time. We fetch these models to generate more accurate schedules that can react to changes in demand.

We propose the following architecture to provide a scalable and feasible solution.

![Sumo-cfg: Ne York City - Traffic Simulation](https://i.ibb.co/Pg57GCr/sumo-ny.png)
