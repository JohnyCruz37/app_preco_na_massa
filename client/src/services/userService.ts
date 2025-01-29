import axios from 'axios';

const API_URL = 'http://localhost:8000/users/';

export interface FormDataPush{
    nome: string;
    email: string;
    celular: string;
    senha: string;
    pro_labore?: number;
}

export const createUser = async (formData: FormDataPush) => {
    const response = await axios.post(API_URL, formData, {
        headers: {
            'Content-Type': 'application/json'
        },
    });
    return response;
};