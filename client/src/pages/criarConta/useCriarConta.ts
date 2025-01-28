import { useState } from "react";
import { validateName, validateLastName, validateEmail, validateConfirmEmail, validatePassword, validateConfirmPassword, validatePhone } from "./validations";
import concatNomeSobrenome from "./concatNomeSobrenome";
import { createUser, FormDataPush } from "../../services/userService";

interface FormData {
    name: string;
    lastName: string;
    email: string;
    confirmEmail: string;
    phone: string;
    password: string;
    confirmPassword: string;
}

interface Errors {
    name?: string | null;
    lastName?: string | null;
    email?: string | null;
    confirmEmail?: string | null;
    phone?: string | null;
    password?: string | null;
    confirmPassword?: string | null;
}

export const useCriarConta = () => {
    const [formData, setFormData] = useState<FormData>({
        name: "",
        lastName: "",
        email: "",
        confirmEmail: "",
        phone: "",
        password: "",
        confirmPassword: ""
    });

    const [errors, setErrors] = useState<Errors>({});

    const handleChange = (e:React.ChangeEvent<HTMLInputElement>) => {
        const { name, value } = e.target;
        setFormData((prev) => ({  ...prev, [name]: value }));
    };

    const handleBlur = (e:React.FocusEvent<HTMLInputElement>) => {
        const { name, value } = e.target;
        const newErrors: Errors = {...errors};

        switch(name) {
            case "name":
                newErrors.name = validateName(value);
                break;
            case "lastName":
                newErrors.lastName = validateLastName(value);
                break;
            case "email":
                newErrors.email = validateEmail(value);
                break;
            case "confirmEmail":
                newErrors.confirmEmail = validateConfirmEmail(formData.email, value);
                break;
            case "phone":
                newErrors.phone = validatePhone(value);
                break;
            case "password":
                newErrors.password = validatePassword(value);
                break;
            case "confirmPassword":
                newErrors.confirmPassword = validateConfirmPassword(formData.password, value);
                break;
        }
        setErrors(newErrors);
    };

    const validateForm = () => {
        const newErrors: Errors = {};
        newErrors.name = validateName(formData.name);
        newErrors.lastName = validateLastName(formData.lastName);
        newErrors.email = validateEmail(formData.email);
        newErrors.confirmEmail = validateConfirmEmail(formData.email, formData.confirmEmail);
        newErrors.phone = validatePhone(formData.phone);
        newErrors.password = validatePassword(formData.password);
        newErrors.confirmPassword = validateConfirmPassword(formData.password, formData.confirmPassword);

        setErrors(newErrors);
        return Object.values(newErrors).every((err) => !err);
    };
    const handleSubmit = async (e: React.FormEvent<HTMLFormElement>) => {
        e.preventDefault();

        if(validateForm()) {
            console.log("Formulário válido");
            const dataPush: FormDataPush = {
                nome: concatNomeSobrenome(formData.name, formData.lastName),
                email: formData.email,
                celular: formData.phone,
                senha: formData.password,
            }
            
            try {
                const response = await createUser(dataPush);
                console.info("Usuário criado com sucesso", response.data);
            } catch (error) {
                console.error("Erro ao criar usuário", error);
            }

        } else {
            console.log("Formulário inválido");
        }
    };

    return {formData, errors, handleChange, handleBlur, handleSubmit};

}

