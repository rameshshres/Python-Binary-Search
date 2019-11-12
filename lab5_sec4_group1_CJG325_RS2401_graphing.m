% Set sample size vector
n = [256, 1024, 4096,16384,65536,262144   ];

# Set vectors for the results of each algorithm

exp_time_rec=[0.00000391,0.00000486,0.00000583,0.00000686, 0.00000773,0.00000872];
exp_time_bin=[0.00000324, 0.00000407, 0.00000479, 0.00000565,0.00000644,0.00000725   ];

% Estimated theoretical C values based on an average of experimental values.

C_bin=0.0000004016;
C_rec=0.000000485 ;  

% Theoretical Run Times

theory_bin= C_bin*log2(n);
theory_rec= C_rec*log2(n);

% Plot all the trends
figure(1)
clf
plot( n, exp_time_bin, 'ro' )

hold on
plot( n, exp_time_rec, 'mo')
plot( n, theory_bin, 'g-' )
plot( n, theory_rec, 'c-' )

hold off

% Make a legend for the trends
legend( 'experimental binry', 'experimental recursive', 'theory binary', 'theory recursive', 'Location', 'northwest' )

% Format axes and title
xlabel( ' list length n ' )
ylabel( 'run time f(n) in sec' )
title( 'Search and compare Algorithms  ' )

set( gcf, 'Color', [ 1 1 1 ] )

% Plot all the trends on a loglog plot.
figure(2)
clf
loglog( n, exp_time_bin, 'ro' )      
hold on
loglog( n, exp_time_rec, 'ko' )    
loglog( n, theory_bin, 'k-' )
loglog( n, theory_rec, 'g-' )
hold off
%set axis label
xlabel('log(n)')
ylabel('log(f(n))')
%set axis title
title('Search and compare Algorithms  log-log Axes')
%set axis legend

legend( 'experimental binary', 'experimental recursive','theory binary','theory recursive','Location', 'northwest')

axis tight