#include <iostream>
#include <fstream>
#include <string>
#include <cstdlib> 
#include <math.h>
 
using namespace std;
 

int main(int args, char * argv[])
{
	int len = 0;
	string dist_vals[12] = {"150", "200", "500", "750", "1000", "1250", "1500", "2000", "3000", "5000", "10000", "20000"}
	double pi = 22.0/7.0;
	char line[50];
	string location[654], line1;
  	double values[1308], lat[654],lon[654];
	ifstream myfile ("Book1.csv");
	if (myfile.is_open())
	{
    	for (int i=0;i<1308;i++)
   		{
     		myfile.getline (line,256);
     		values[i] = atof(line); //convert to double
    	}
    	for (int i=0;i<654;i++)
		{
			getline (myfile, line1);
			location[i] = line1;
			cout<<location[i]<<endl;
		}
	myfile.close();
	}

	else cout << "Unable to open file"; 
  
	for (int i=0;i<654;i++)
	{
    	lat[i] = values[i];
    	lon[i] = values[i+654];
	}
    
	ofstream opfile;

	for (int i = 0; i<12; i++)
	{
 		opfile.open("sample2_"+dist_vals[i]+".csv"); 
		if (opfile.is_open())
		{
			opfile << "Latitude, Longitude, Location 1, Latitude, Longitude, Location 2, Distance between locations" << endl;
		}
		else 
			std::cout<<"ERROR";

    	for (int i =0;i<654;i++)
    	{
			for (int j =i+1;j<654;j++)
			{
    			dist = acos (sin (lat[i]*pi/180)*sin (lat[j]*pi/180) + cos (lat[i]*pi/180)*cos (lat[j]*pi/180) * cos ((lon[j] -lon[i])*pi/180))*6370000.0;
    			cout<<"\n Distance between latitude,longitude "<<i+1<<" and "<<j+1<<" is "<<dist<<" meters"<<endl;
    			if (dist<atof(dist_vals[i]) && dist!=0.0) 
    			{
    				opfile<<lat[i]<<","<<lon[i]<<","<<location[i]<<","<<lat[j]<<","<<lon[j]<<","<<location[j]<<","<<dist<<endl;	
				}
			}
		}	
		opfile.close();
	}
	return 0;
} 
