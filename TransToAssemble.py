import os
import re

regs=['t1','t2','t3','t4','t5','t6','t7','t8','t9','s0','s1','s2','s3','s4']
table={}
reg_ok={}
variables=[]

def translate(line):
    if line[0]=='LABEL':
        return line[1]+':'
    if line[1]==':=':
        if len(line)==3:
            if line[-1][0]=='#':
                return '\tli %s,%s'%(Get_R(line[0]),line[-1].replace('#',''))
            else:
                return '\tmove %s,%s'%(Get_R(line[0]),Get_R(line[2]))
        if len(line)==5:
            if line[3]=='+':
                if line[-1][0]=='#':
                    return '\taddi %s,%s,%s'%(Get_R(line[0]),Get_R(line[2]),line[-1].replace('#',''))
                else:
                    return '\tadd %s,%s,%s'%(Get_R(line[0]),Get_R(line[2]),Get_R(line[-1]))
            elif line[3]=='-':
                if line[-1][0]=='#':
                    return '\taddi %s,%s,-%s'%(Get_R(line[0]),Get_R(line[2]),line[-1].replace('#',''))
                else:
                    return '\tsub %s,%s,%s'%(Get_R(line[0]),Get_R(line[2]),Get_R(line[-1]))
            elif line[3]=='*':
                return '\tmul %s,%s,%s'%(Get_R(line[0]),Get_R(line[2]),Get_R(line[-1]))
            elif line[3]=='/':
                return '\tdiv %s,%s\n\tmflo %s'%(Get_R(line[2]),Get_R(line[-1]),Get_R(line[0]))
            elif line[3]=='%':
                return '\trem %s,%s,%s'%(Get_R(line[0]),Get_R(line[2]),Get_R(line[-1]))
            elif line[3]=='<':
                return '\tslt %s,%s,%s'%(Get_R(line[0]),Get_R(line[2]),Get_R(line[-1]))
            elif line[3]=='>':
                return '\tslt %s,%s,%s'%(Get_R(line[0]),Get_R(line[-1]),Get_R(line[2]))
            elif line[3]=='==':
                return '\tslt $s5,%s,%s\n\tslt $s6,%s,%s\n\tsub $s7,$s5,$s6\n\tabs $s6,$s7\n\tsubi $s7,$s6,1\n\tabs %s,$s7'%(Get_R(line[2]),Get_R(line[-1]),Get_R(line[-1]),Get_R(line[2]),Get_R(line[0]))
            elif line[3]=='&&':
                return '\tand %s,%s,%s'%(Get_R(line[0]),Get_R(line[2]),Get_R(line[-1]))
            elif line[3]=='||':
                return '\tor %s,%s,%s'%(Get_R(line[0]),Get_R(line[2]),Get_R(line[-1]))
            else:
                return 'error'
        if line[2]=='CALL':
            if line[3]=='read' or line[3]=='print':
                return '\taddi $sp,$sp,-4\n\tsw $ra,0($sp)\n\tjal %s\n\tlw $ra,0($sp)\n\tmove %s,$v0\n\taddi $sp,$sp,4'%(line[-1],Get_R(line[0]))
            else:
                return '\taddi $sp,$sp,-24\n\tsw $t0,0($sp)\n\tsw $ra,4($sp)\n\tsw $t1,8($sp)\n\tsw $t2,12($sp)\n\tsw $t3,16($sp)\n\tsw $t4,20($sp)\n\tjal %s\n\tlw $a0,0($sp)\n\tlw $ra,4($sp)\n\tlw $t1,8($sp)\n\tlw $t2,12($sp)\n\tlw $t3,16($sp)\n\tlw $t4,20($sp)\n\taddi $sp,$sp,24\n\tmove %s $v0'%(line[-1],Get_R(line[0]))
    if line[0]=='GOTO':
        return '\tj %s'%line[1]
    if line[0]=='RETURN':
            return '\tmove $v0,%s\n\tjr $ra'%Get_R(line[1])
    if line[0]=='IF':
        if line[2]=='==':
            return '\tbeq %s,%s,%s'%(Get_R(line[1]),Get_R(line[3]),line[-1])
        if line[2]=='!=':
            return '\tbne %s,%s,%s'%(Get_R(line[1]),Get_R(line[3]),line[-1])
        if line[2]=='>':
            return '\tbgt %s,%s,%s'%(Get_R(line[1]),Get_R(line[3]),line[-1])
        if line[2]=='<':
            return '\tblt %s,%s,%s'%(Get_R(line[1]),Get_R(line[3]),line[-1])
        if line[2]=='>=':
            return '\tbge %s,%s,%s'%(Get_R(line[1]),Get_R(line[3]),line[-1])
        if line[2]=='<=':
            return '\tble %s,%s,%s'%(Get_R(line[1]),Get_R(line[3]),line[-1])
        if line[2]=='&&':
            return '\tand $s7,%s,%s\n\tbnez $s7,%s'%(Get_R(line[1]),Get_R(line[3]),line[-1])
        if line[2]=='||':
            return '\tor $s7,%s,%s\n\tbnez $s7,%s'%(Get_R(line[1]),Get_R(line[3]),line[-1])
        else:
            return '\terror'
    if line[0]=='FUNCTION':
        return '%s:'%line[1]
    if line[0]=='CALL':
        if line[-1]=='read' or line[-1]=='print':
            return '\taddi $sp,$sp,-4\n\tsw $ra,0($sp)\n\tjal %s\n\tlw $ra,0($sp)\n\taddi $sp,$sp,4'%(line[-1])
        else:
            return '\taddi $sp,$sp,-24\n\tsw $t0,0($sp)\n\tsw $ra,4($sp)\n\tsw $t1,8($sp)\n\tsw $t2,12($sp)\n\tsw $t3,16($sp)\n\tsw $t4,20($sp)\n\tjal %s\n\tlw $a0,0($sp)\n\tlw $ra,4($sp)\n\tlw $t1,8($sp)\n\tlw $t2,12($sp)\n\tlw $t3,16($sp)\n\tlw $t4,20($sp)\n\taddi $sp,$sp,24\n\tmove %s $v0'%(line[-1],Get_R(line[0]))
    if line[0]=='ARG':
        return '\tmove $t0,$a0\n\tmove $a0,%s'%Get_R(line[-1])
    if line[0]=='PARAM':
        table[line[-1]]='a0'
    return ''

def write_to_txt(Obj):
    f=open('Assemble.asm','w')
    template='''
.data
_prompt: .asciiz "Enter an integer:"
_ret: .asciiz "\\n"
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
'''
    f.write(template)
    for line in Obj:
        f.write(line+'\n')
    f.close()

def Load_Var(Inter):
    global variables
    temp_re='(temp\d+)'
    for line in Inter:
        temps=re.findall(temp_re,' '.join(line))
        variables+=temps

def Load_Inter(filename):
    lines=[]
    for line in open(filename,'r',encoding='utf-8'):
        line=line.replace('\r','').replace('\n','')
        if line =='':
            continue
        lines.append(line.split(' '))
    return lines

def Get_R(string):
    try:
        variables.remove(string)
    except:
        pass
    if string in table:
        return '$'+table[string]  
    else:
        keys=[]
        for key in table:        
            keys.append(key)
        for key in keys:          
            if 'temp' in  key and key not in variables:
                reg_ok[table[key]]=1
                del table[key]
        for reg in regs:        
            if reg_ok[reg]==1:   
                table[string]=reg 
                reg_ok[reg]=0     
                return '$'+reg




def parser():
    for reg in regs:
        reg_ok[reg]=1 
    Inter=Load_Inter('InterCode.txt')  
    Load_Var(Inter)   
    Obj=[]
    for line in Inter:
        obj_line=translate(line) 
        if obj_line=='':
            continue
        Obj.append(obj_line)
    write_to_txt(Obj)

parser()
