/*
Projectile motion C++ codes
*/

#include<iostream>
#include<cmath>

using namespace std;

int main()

{
	long double pi=M_PI, g, v, a, h, H, D, T, r, x, y, z, w, e, s;
	
	cout<<"PROJECTILE MOTION OF OBJECT AT A PARTICULAR PLANET \n\n";
	cout<<"Non Trivial Mathematical Problem:\n "<<endl;
	cout<<" An object is thrown/launched at a particular planet with gravity g.\n";
	cout<<" The object is thrown/launched at initial velocity v, with angle of elevation a,\n";
	cout<<" and at the height h.\n";
	cout<<" Note that g is measured in meter per second square,\n v is measured in meter per second,"; 
	cout<<" a is measured in degrees, \n and h is measured in meters.";
	cout<<" Assuming that the air resistance is negligible.\n";
	cout<<" Find the following:\n\n";
	cout<<"  (a) The distance where the object will land.\n";
	cout<<"  (b) The maximum height that the object can reach.\n";
	cout<<"  (c) The speed of impact of the object to the ground when it lands.\n";
	cout<<"  (d) The time of impact to the ground.\n";
	cout<<"  (e) The function f(x) of the trajectory of the object in xy-plane.\n";
	cout<<"  (f) The position vector r(t) of the trajectory of the object in xy-plane.\n\n";
	cout<<" Enter initial velocity v of the object (meter per second): ";
	cin>> v;
	cout<<"\n";
	if(v>0){
	
	cout<<" Enter angle of elevation a (between 0 degrees and 90 degrees): ";
	cin>> a;
	cout<<"\n";
	if(a>0,a<90){
	
	cout<<" Enter gravity g of the planet (meter per second square): ";
	cin>>g;
	cout<<"\n";
	if(g>0){
	
	cout<<" Enter the height h where the object thrown/launched (meters): ";
	cin>>h;
	cout<<"\n";
	if(h>0){
	
	//formulas
	
	r = a*(pi/180);
	H = (v*v)*(sin(r)*sin(r))/(2*g)+h;
	T = (v*sin(r) + sqrt(v*v*sin(r)*sin(r)+2*g*h))/g;
	D = v*cos(r)*T;
	s = sqrt(v*v + 2*g*h);
	x = tan(r);
	y = -g/(2*v*v*cos(r)*cos(r));
	z = v*cos(r);
	w = v*sin(r);
	e = g/2; 
	
	
	cout<<"\n\n";
	
	cout<<"GIVEN\n\n";
	cout<<" g = "<<g<<" meter per second square\n\n";
	cout<<" v = "<<v<<" meter per second\n\n";
	cout<<" a = "<<a<<" degrees\n\n";
	cout<<" h = "<<h<<" meter/meters\n\n";
	cout<<"RESULTS\n\n";
	cout<<" (a) The distance where the object will land is "<<D<<" meters."<<endl;
	cout<<"\n";
	cout<<" (b) The maximum height that the object can reach is "<<H<<" meters."<<endl;
	cout<<"\n";
	cout<<" (c) The speed of impact of the object to the ground when it lands is "<<s<<" meter per second."<<endl;
	cout<<"\n";
	cout<<" (d) The time of impact to the ground is "<<T<<" seconds."<<endl;
	cout<<"\n";
	cout<<" (e) The function of the trajectory of the object in xy-plane is f(x)= "<<y<<"x^2 + "<<x<<"x + "<<h<<", 0 < x < "<<D<<".\n";
	cout<<"\n";
	cout<<" (f) The position vector of the trajectory of the object in xy-plane is r(t)=<"<<z<<"t, "<<w<<"t - "<<e<<"t^2 + "<<h<<">, 0 < t < "<<T<<".";
	cout<<"\n\n\n\n\n";
	
}
	else{
		cout<<"\n\n                       ERROR!!! \n\n                      TRY AGAIN\n\n                      Note h > 0 \n\n\n\n\n";
		return main();
	}
}
	else{
		cout<<"\n\n                       ERROR!!! \n\n                      TRY AGAIN\n\n                      Note g > 0 \n\n\n\n\n";
		return main();
	}
}	
	
	else{
		cout<<"\n\n                       ERROR!!! \n\n                      TRY AGAIN\n\n                     Note 0 < a < 90 \n\n\n\n\n";
		return main();
	}
}

	else{
		cout<<"\n\n                       ERROR!!! \n\n                      TRY AGAIN\n\n                      Note v > 0 \n\n\n\n\n";
		return main();
	}
	}
	


