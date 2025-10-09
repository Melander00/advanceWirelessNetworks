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