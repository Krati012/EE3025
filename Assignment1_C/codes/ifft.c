#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <complex.h>
#include <string.h>

//IFFT implemented in a divide and conquer approach using recursive function
void ifft(double complex* x, int n){
    //base case
    if (n == 1)
        return;
    //allocating memory for storing even and odd parts of x
    double complex* odd = malloc(n/2 * sizeof(double complex));
    double complex* even = malloc(n/2 * sizeof(double complex));
    //splitting x into even and odd components
    for(int i = 0; 2 * i < n; i++) {
        even[i] = x[2 * i];
        odd[i] = x[2 * i + 1];
    }
    //calculating ifft of even and odd component recursively
    ifft(even, n/2);
    ifft(odd, n/2);
    //combining the even and odd parts
    double complex w;
    for(int j = 0; 2 * j < n; j++) {
        w = CMPLX(cos(-2*M_PI*j/n), sin(-2*M_PI*j/n));
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
    
    double complex* X = (double complex*)malloc(n * sizeof(double complex));
    double complex* H = (double complex*)malloc(n * sizeof(double complex));
    double complex* Y = (double complex*)malloc(n * sizeof(double complex));

    double complex* ifft_Y = (double complex*)malloc(n * sizeof(double complex));
    
    FILE *fin1,*fin2,*fout1;

    //Reading fft of x .dat file
    fin1 = fopen("fft_X.dat","r");
    int count = 0;
    double a,b;
    while (!feof(fin1) && count < n) 
    {
        fscanf(fin1, "%lf+%lfi \n", &a, &b);
        X[count] = CMPLX(a,b);
        count++;
    }
    
    //Reading fft of H .dat file
    fin2 = fopen("fft_H.dat","r");
    count = 0;
    while (!feof(fin2) && count < n) 
    {
        fscanf(fin2, "%lf+%lfi \n", &a, &b);
        H[count] = CMPLX(a,b);
        count++;
    }

    //DFT of Y=X*H
    for(int i=0;i<n;i++)
    {
        Y[i] = H[i]*X[i];
        ifft_Y[i] = Y[i];
    }

    //Inverse fft of Y
	ifft(ifft_Y,n);
	fout1 = fopen("ifft_Y.dat","w");
    for(int i=0;i<n;i++)
    {
        fprintf(fout1,"%lf \n",creal(ifft_Y[i]/10e5));
    }

    fclose(fin1);
    fclose(fin2);
    fclose(fout1);
    return 0;    
}
