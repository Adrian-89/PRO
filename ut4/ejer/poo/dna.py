from __future__ import annotations


class DNA:
    ADENINE = 'A'
    CYTOSINE = 'C'
    GUANINE = 'G'
    THYMINE = 'T'

    def __init__(self, sequence: str): 
        self.sequence = sequence

    def __str__(self): 
        return f'{self.sequence}'
    
    @property
    def adenines(self) -> int:
        """Número de adeninas de la secuencia de ADN"""
        return self.sequence.count(DNA.ADENINE)

    @property
    def cytosines(self) -> int:
        """Número de citosinas de la secuencia de ADN"""
        return self.sequence.count(DNA.CYTOSINE)

    @property
    def guanines(self) -> int:
        """Número de guaninas de la secuencia de ADN"""
        return self.sequence.count(DNA.GUANINE)

    @property
    def thymines(self) -> int:
        """Número de timinas de la secuencia de ADN"""
        return self.sequence.count(DNA.THYMINE)

    def __add__(self, other: DNA) -> DNA:
        """Se define la suma de dos secuencias de ADN como el máximo de cada base nitrogenada
        (base a base). Por ejemplo 'T' sería mayor que 'A'.
        Si las secuencias no tienen la misma longitud, habrá que aplicar el máximo base a base
        hasta donde se pueda, y completar el resto de la secuencia con la parte que falte, bien
        de la primera o bien de la segunda secuencia, en función de cuál sea mayor.
        """
        sequence_number2 = ''
        for dna1, dna2 in zip(self.sequence, other.sequence):
            if dna1 == DNA.ADENINE and dna2 == DNA.THYMINE;
                sequence_number2 += DNA.THYMINE
            elif dna1 == DNA.THYMINE and dna2 == DNA.ADENINE;
                sequence_number2 += DNA.THYMINE
            elif dna1 == DNA.CYTOSINE and dna2 == DNA.ADENINE;
                sequence_number2 += DNA.CYTOSINE
            elif dna1 == DNA.ADENINE and dna2 == DNA.CYTOSINE;
                sequence_number2 += DNA.CYTOSINE
            elif dna1 == DNA.GUANINE and dna2 == DNA.THYMINE;
                sequence_number2 += DNA.THYMINE
            elif dna1 == DNA.THYMINE and dna2 == DNA.GUANINE;
                sequence_number2 += DNA.THYMINE
            elif dna1 == DNA.CYTOSINE and dna2 == DNA.ADENINE;
                sequence_number2 += DNA.CYTOSINE
    def __len__(self):
        """Longitud de la secuencia de ADN"""
        return len(self.sequence)

    def stats(self) -> dict[str, float]:
        """Porcentaje de aparición de cada base con respecto al total.
        Se devuelve un diccionario donde la clave será la base nitrogenada
        y el valor será el porcentaje."""
        ...

    def __mul__(self, other: DNA) -> DNA:
        """Se define la multiplicación de dos secuencias de ADN como una nueva cadena
        de ADN donde aparecen las bases que son iguales (posición a posición)"""
        ...

    @classmethod
    def build_from_file(cls, path: str) -> DNA:
        """Construye una secuencia de ADN a partir de un fichero.
        El formato del fichero es tener una única línea con todas las bases
        una detrás de otra."""
        ...

    def dump_to_file(self, path: str) -> None:
        """Vuelca una secuencia de ADN a un fichero de salida.
        El formato del fichero es tener una única línea con todas las bases
        una detrás de otra."""
        ...

    def __getitem__(self, index: int) -> str:
        """Devuelve la base que ocupa la posición 'index'"""
        ...

    def __setitem__(self, index: int, base: str) -> None:
        """Fija la base 'base' en la posición 'index'"""
        ...
