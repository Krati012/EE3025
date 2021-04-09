#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <complex.h>
#include <math.h>

int main(){
	int n = (1<<20);
	FILE *fin, *fout1, *fout2;
    //Taking x.dat as input
	fin = fopen("x.dat","r");
	double* x = (double*)malloc(n * sizeof(double));
	double* y = (double*)malloc(n * sizeof(double));
    //coefficient values computed from difference equation
	double a[] = {1,-2.52,2.56,-1.206,0.22013};
	double b[] = {0.00345,0.0138,0.020725,0.0138,0.00345};
	int count=0;
	while (!feof(fin) && count < n) 
    {
        double val;
        fscanf(fin, "%lf", &val);
        x[count++] = val;
    }
    //Defining output y using input and a,b values
    y[0] = (b[0]/a[0])*x[0];
	y[1] = (1/a[0])*(b[0]*x[1]+b[1]*x[0] - a[1]*y[0]);
	y[2] = (1/a[0])*(b[0]*x[2]+b[1]*x[1]+b[2]*x[0]- 
			a[1]*y[1]-a[2]*y[0]);
	y[3] = (1/a[0])*(b[0]*x[3]+b[1]*x[2]+b[2]*x[1]+
			b[3]*x[0] - a[1]*y[2]-a[2]*y[1]-a[3]*y[0]);
	y[4] = (1/a[0])*(b[0]*x[4]+b[1]*x[3]+b[2]*x[2]+
			b[3]*x[1]+b[4]*x[0] - a[1]*y[3]-a[2]*y[2]-
			a[3]*y[1]-a[4]*y[0]);
    for(int i=5;i<n;i++){
		y[i] = (1/a[0])*(b[0]*x[i]+b[1]*x[i-1]+b[2]*x[i-2]+
		b[3]*x[i-3]+b[4]*x[i-4] - a[1]*y[i-1]-a[2]*y[i-2]-
		a[3]*y[i-3]-a[4]*y[i-4]);
	}
    //Writing input and output data into .dat files
    fout1  = fopen("xn.dat", "w");
    for(int i = 0; i < n; i++){
        fprintf(fout1, "%lf \n", x[i]);
    }
    fout2  = fopen("yn.dat", "w");
    for(int i = 0; i < n; i++){
        fprintf(fout2, "%lf \n", y[i]);
    }
    fclose(fin);
    fclose(fout1);
    fclose(fout2); 
    return 0;
}