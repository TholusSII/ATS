set table "gnuplot/ALL_EXOS/1.table"; set format "%.5f"
set samples 100.0; set parametric; plot [t=-3:1] [] [] log10(10**t),(t<log10(1/(10.))?20*log10(15.):+20*log10(15./(10.))-20*log10(10**t))
