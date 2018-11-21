#!/bin/bash

time ./insilico_PN90_LN30_noise_noPN-PN_1000.out -o ./PN90_LN30_1000_g0-05LN0-125LNPN0-05PNLN0-0875PN_PN10LN5.csv -n ./nsets/1000/nsets_AL120_PN10LN5_1000.isf -s ./noPN-PN/ssets_AL120_g0-05LN0-125LNPN0-05PNLN0-0875PN.isf > ./PN90_LN30.log

time ./insilico_PN90_LN30_noise_noPN-PN_1000.out -o ./PN90_LN30_1000_g0-05LN0-125LNPN0-05PNLN0-0875PN_PN15LN7.csv -n ./nsets/1000/nsets_AL120_PN15LN7_1000.isf -s ./noPN-PN/ssets_AL120_g0-05LN0-125LNPN0-05PNLN0-0875PN.isf > ./PN90_LN30.log

time ./insilico_PN90_LN30_noise_noPN-PN_1000.out -o ./PN90_LN30_1000_g0-05LN0-125LNPN0-05PNLN0-0875PN_PN20LN10.csv -n ./nsets/1000/nsets_AL120_PN20LN10_1000.isf -s ./noPN-PN/ssets_AL120_g0-05LN0-125LNPN0-05PNLN0-0875PN.isf > ./PN90_LN30.log


