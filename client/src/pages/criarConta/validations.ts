export const validateName = (name: string):string | null => {
    if(!name.trim()) return "Nome é obrigatório"
    if(name.length < 3) return "Nome deve ter no mínimo 3 caracteres."
    return null;
}

export const validateLastName = (lastName: string):string | null => {
    if(!lastName.trim()) return "Sobrenome é obrigatório"
    if(lastName.length < 3) return "Sobrenome deve ter no mínimo 3 caracteres."
    return null;
}


export const validateEmail = (email: string):string | null => {
    if(!email.trim()) return "E-mail é obrigatório"
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if(!emailRegex.test(email)) return "Formato do E-mail inválido"
    return null;
}

export const validateConfirmEmail = (email: string, confirmEmail: string):string | null => {
    if(email !== confirmEmail) return "E-mails não conferem."
    return null;
}


export const validatePhone = (phone: string):string | null => {
    if(!phone.trim()) return "Celular é obrigatório"
    if(phone.length < 11) return "Celular deve ter no mínimo 11 caracteres."
    return null;
}


export const validatePassword = (password: string):string | null => {
    if(!password.trim()) return "Senha é obrigatória"
    if(password.length < 8) return "Senha deve ter no mínimo 8 caracteres."
    if(password.length > 20) return "Senha deve ter no máximo 20 caracteres."
    if(!/[a-z]/.test(password)) return "Senha deve conter ao menos uma letra minúscula."
    if(!/[A-Z]/.test(password)) return "Senha deve conter ao menos uma letra maiúscula."
    if(!/[0-9]/.test(password)) return "Senha deve conter ao menos um número."
    if(!/[!@#$%^&*]/.test(password)) return "Senha deve conter ao menos um caractere especial."
    return null;
}

export const validateConfirmPassword = (password: string, confirmPassword: string):string | null => {
    if(password !== confirmPassword) return "Senhas não conferem."
    return null;
}
