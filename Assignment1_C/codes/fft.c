#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <complex.h>
#include <string.h>

//FFT implemented in a divide and conquer approach using recursive function
void fft(double complex* x, int n){
    //base case
    if (n == 1)
        return;
    //allocating memory for even and odd parts of x
    double complex* odd = malloc(n/2 * sizeof(double complex));
    double complex* even = malloc(n/2 * sizeof(double complex));
    //splitting x into even and odd components 
    for(int i = 0; 2 * i < n; i++) {
        even[i] = x[2 * i];
        odd[i] = x[2 * i + 1];
    }
    //calculating fft of even and odd component recursively
    fft(even, n/2);
    fft(odd, n/2);
    //combining the even and odd parts
    double complex w; 
    for(int j = 0; 2 * j < n; j++) {
        w = CMPLX(cos(2*M_PI*j/n), sin(2*M_PI*j/n));
        x[j] = even[j] + w * odd[j];
        x[j + n/2] = even[j] - w * odd[j];
    }
    //freeing the memory allocated to even and odd
    free(even);
    free(odd);
}

int main()
{
    int n= (1<<20);
    double* x = (double*)malloc(n * sizeof(double));
    double* h = (double*)malloc(n * sizeof(double));
    
    double complex* X = (double complex*)malloc(n * sizeof(double complex));
    double complex* H = (double complex*)malloc(n * sizeof(double complex));
    
    FILE *fin1,*fout1,*fout2,*fout3;
    //Taking .dat file of x as input
    fin1 = fopen("x.dat","r");
    int count=0;
    while (!feof(fin1) && count < n) 
    {
        fscanf(fin1, "%lf", &(x[count]));
        X[count] = CMPLX(x[count],0);
        count++;
    }
    //Calculating FFT of x
    fft(X,n);
    fout1 = fopen("fft_X.dat","w");
    for(int i=0;i<n;i++)
    {
        fprintf(fout1,"%lf+%lfi \n",creal(X[i]),cimag(X[i]));
    }

    //Taking h from the difference equation
    double a[] = {1,-2.52,2.56,-1.206,0.22013};
    double b[] = {0.00345,0.0138,0.020725,0.0138,0.00345};

    h[0] = (b[0]/a[0]);
    h[1] = (1/a[0])*(b[1] - a[1]*h[0]);
    h[2] = (1/a[0])*(b[2]- a[1]*h[1]-a[2]*h[0]);
    h[3] = (1/a[0])*(b[3] - a[1]*h[2]-a[2]*h[1]-a[3]*h[0]);
    h[4] = (1/a[0])*(b[4] - a[1]*h[3]-a[2]*h[2]-a[3]*h[1]-a[4]*h[0]);
    for(int i=0; i<5;i++)
        H[i] = CMPLX(h[i],0);
    for(int i=5;i<n;i++){
        h[i] = (1/a[0])*(0 - a[1]*h[i-1]-a[2]*h[i-2]-a[3]*h[i-3]-a[4]*h[i-4]);
        H[i] = CMPLX(h[i],0);
    }
    //Calculating FFT of h
    fft(H,n);
    fout2 = fopen("fft_H.dat","w");
    for(int i=0;i<n;i++)
    {
        fprintf(fout2,"%lf+%lfi \n",creal(H[i]),cimag(H[i]));
    }

    fclose(fin1);
    fclose(fout1);
    fclose(fout2);

    return 0;
}