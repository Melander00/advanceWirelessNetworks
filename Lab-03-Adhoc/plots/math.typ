#let eq(body) = {
  math.equation(body, block: true, numbering: "(1)")
}

#eq[$D  = 8 dot 10^9$]
#eq[$p = (1 - "BER")^P$]
#eq[$N = D/(P - H)$]
#eq[$M = 2N - N p = N(2 - p)$]
#eq[$B = M P$]
#eq[$T = B/R$]

#eq[$

  B = N(2 - p)P = D (2 - p)(P)/(P - H) \
  T = (D P (2-p))/(R (P - H)) = (D P (2-(1 - "BER")^P))/(R (P - H))
  
  $]

#eq[$
  T = (D P )/(R (P - H)) (2-(1 - "BER")^P)
$]


== Alternative

#eq[$

cases(

    D ", application data size",
    P ", packet size in bits",
    H ", packet header size in bits",
    p = (1 - "BER")^P ", probablity that a packet is transmitted successfully", 
    N = D / (P - H) ", number of packets to transmit",
    R ", bits/second"
)      
      
$]

The expected number of transmission per packet is 
#eq[$E = 1/p$]
which means that the expected number of packets to send (including retransmissions) is
#eq[$M = N/p$]
The amount of bits to transmit in total is
#eq[$B = M P$]
The total amount of time required to transmit all those bits are
#eq[$T = B/R$]
The final equation becomes
#eq[$
    T &= (M P) / R \
      &= N/p P/R \
      &=  D/(P - H) P/(R p) \
    T &= D/R P/(P - H) 1/(1 - "BER")^P
$]