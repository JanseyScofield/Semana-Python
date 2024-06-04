from fpdf import FPDF

descricao = input("Digite a descrição do projeto: ")
horasEstimadas = int(input("Digite a quantidade de horas estimadas: "))
valorHora = float(input("Digite o valor da hora trabalhada: "))
prazoEntrega = input("Digite o prazo para entrega: ")

valorTotal = horasEstimadas*valorHora

pdf = FPDF()
pdf.add_page()
pdf.image("aula01/modelo.png",x=0, y=0)
pdf.set_font("Arial")
pdf.text(115, 145, descricao)
pdf.text(115, 160, str(horasEstimadas))
pdf.text(115, 175, str(valorHora))
pdf.text(115, 190, prazoEntrega)
pdf.text(115, 205, str(valorTotal))
pdf.output("Orçamento.pdf")
print("PDF criado com sucesso!")