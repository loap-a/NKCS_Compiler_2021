
.data
_prompt: .asciiz "Enter an integer:"
_ret: .asciiz "\n"
.globl main
.text
read:
    li $v0,4
    la $a0,_prompt
    syscall
    li $v0,5
    syscall
    jr $ra

print:
    li $v0,1
    syscall
    li $v0,4
    la $a0,_ret
    syscall
    move $v0,$0
    jr $ra
main:
	li $t1,2
	move $t2,$t1
	addi $sp,$sp,-4
	sw $ra,0($sp)
	jal read
	lw $ra,0($sp)
	move $t1,$v0
	addi $sp,$sp,4
	move $t2,$t1
	li $t1,100
	add $t3,$t2,$t1
	li $t1,2
	rem $t4,$t3,$t1
	move $t0,$a0
	move $a0,$t4
	addi $sp,$sp,-4
	sw $ra,0($sp)
	jal print
	lw $ra,0($sp)
	addi $sp,$sp,4
	li $t1,0
	move $t3,$t1
	li $t1,3
	move $t4,$t1
	li $t1,1
	move $t5,$t1
label0:
	li $t1,0
	slt $t6,$t1,$t4
	bgt $t4,$t1,label1
	j label2
label1:
	mul $t1,$t5,$t4
	move $t5,$t1
	li $t1,1
	sub $t6,$t4,$t1
	move $t4,$t6
	j label0
label2:
	li $t1,100
	rem $t6,$t5,$t1
	move $t0,$a0
	move $a0,$t6
	addi $sp,$sp,-4
	sw $ra,0($sp)
	jal print
	lw $ra,0($sp)
	addi $sp,$sp,4
	li $t1,0
	move $t6,$t1
label3:
	li $t1,100
	rem $t7,$t5,$t1
	li $t1,1
	sub $t8,$t7,$t1
	slt $t1,$t6,$t8
	blt $t6,$t8,label4
	j label5
label4:
	li $t1,1
	add $t7,$t6,$t1
	move $t1,$t7
label6:
	li $t7,100
	rem $t8,$t5,$t7
	li $t7,1
	sub $t9,$t8,$t7
	slt $t7,$t1,$t9
	blt $t1,$t9,label7
	j label8
label7:
	li $t7,5
	sub $t8,$t1,$t7
	slt $s5,$t8,$t6
	slt $s6,$t6,$t8
	sub $s7,$s5,$s6
	abs $s6,$s7
	subi $s7,$s6,1
	abs $t7,$s7
	beq $t6,$t8,label9
	j label10
label9:
	li $t9,1
	j label11
label10:
	li $t9,0
label11:
	li $s0,2
	add $s1,$t9,$s0
	slt $s5,$s1,$t1
	slt $s6,$t1,$s1
	sub $s7,$s5,$s6
	abs $s6,$s7
	subi $s7,$s6,1
	abs $t9,$s7
	li $s0,3
	sub $s1,$t1,$s0
	slt $s5,$s1,$t6
	slt $s6,$t6,$s1
	sub $s7,$s5,$s6
	abs $s6,$s7
	subi $s7,$s6,1
	abs $s0,$s7
	and $s1,$t9,$s0
	or $t9,$t7,$s1
	or $s7,$t7,$s1
	bnez $s7,label12
	j label13
label12:
	li $t7,1
	add $t9,$t6,$t7
	rem $t7,$t1,$t9
	move $t3,$t7
	move $t0,$a0
	move $a0,$t3
	addi $sp,$sp,-4
	sw $ra,0($sp)
	jal print
	lw $ra,0($sp)
	addi $sp,$sp,4
	j label14
label13:
	li $t7,3
	add $t9,$t6,$t7
	slt $s5,$t1,$t9
	slt $s6,$t9,$t1
	sub $s7,$s5,$s6
	abs $s6,$s7
	subi $s7,$s6,1
	abs $t7,$s7
	li $t9,2
	rem $s0,$t1,$t9
	li $t9,0
	slt $s5,$s0,$t9
	slt $s6,$t9,$s0
	sub $s7,$s5,$s6
	abs $s6,$s7
	subi $s7,$s6,1
	abs $t9,$s7
	and $s0,$t7,$t9
	and $s7,$t7,$t9
	bnez $s7,label15
	j label16
label15:
	li $t7,1
	add $t9,$t6,$t7
	div $t1,$t9
	mflo $t7
	move $t3,$t7
	move $t0,$a0
	move $a0,$t3
	addi $sp,$sp,-4
	sw $ra,0($sp)
	jal print
	lw $ra,0($sp)
	addi $sp,$sp,4
	j label17
label16:
	move $t0,$a0
	move $a0,$t3
	addi $sp,$sp,-4
	sw $ra,0($sp)
	jal print
	lw $ra,0($sp)
	addi $sp,$sp,4
label17:
label14:
	li $t7,1
	move $t9,$t1
	add $t1,$t1,$t7
	j label6
label8:
	li $t7,1
	add $t9,$t6,$t7
	move $t6,$t9
	j label3
label5:
	li $t7,0
	move $v0,$t7
	jr $ra
