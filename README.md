# RSA-Algorithm-Group-Assignment
Hello Welcome to This RSA project done by Addis Ababa Institute of Technology Students. This project use modular arithmetic to encrypt and decrypt a message.
Modular arithmetic is so important in today's word to keep the credentiality of a message across the internet.
so Our project uses two randomly  generated prime numbers called p and q. 
then by uising oilers totient function it generate the values of phi = (p-1)*(q-1)
it generates a number that is coprime with phi called e
by using e and the prooduct of p and q , it generates a public key (e,p*q) 
the by using the e it generates a number that is the inverse of e called d
then it generates a private key (d,p*q)
then to encypt M*(message encypted) = rem((m(message to be encrypted))^e,n)
to decrypt m(message to be decypted ) = rem(m*(message encrypted ))^d,n)

