
% Jouer d'abord la simulation "puissance.slx"

% Récupérer les données de la simulation
U=out.voltage.data;

N=length(U) % Longueur de l'échantillon

% Creation de l'échelle temporelle
t=(0:N-1)*Te;

% Plot de la trace
figure(1) % Première figure, on peut en définir plusieurs selon le numéro
plot(t,U)
title("Signal mesuré") % ajoute un titre
grid                   % ajoute la grille sur le graphique

% Calcul de la FFT
fU=fft(U);
fUabs=abs(fU);
figure(2)
plot(fUabs,'x')
title('FFT avec période trop grande')
grid

% Ajustement de la période, on ne prend pas le dernier point
Uperiod=U(1:N-1);
fUperiod=fft(Uperiod);
fUpabs=abs(fUperiod)
figure(3)
plot(fUpabs,'x')
title('FFT avec période ajustée')
grid

% Calcul de l'échelle de fréquence
N=N-1; % Définit la longueur qu'on veut

DF=1/(Te*N);
Fscale=(0:N-1)*DF;
figure(4)
plot(Fscale, fUpabs,'x')
title('FFT avec période ajustée')
grid

% Présentation de la FFT de façon symétrique
fUpabs1=fftshift(fUpabs); % est équivalent à fUpabs = [fUpabs(1:N/2-1);fUpabs(1:N/2)];
fUpabs2 = [fUpabs(N/2+1:N);fUpabs(1:N/2)];

Fscale=[-N/2:N/2-1]*DF
figure(5)
plot(Fscale, fUpabs1,'x')
title('FFT centrée')
grid



