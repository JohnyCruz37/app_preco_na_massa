import React, {useEffect} from 'react';
import style from "./Alert.module.css"

interface AlertProps {
    type: string;
    message: string;
    onClose: () => void;
}

export const Alert: React.FC<AlertProps> = ({type, message, onClose}) => {
    useEffect(()=>{
        const timer = setTimeout(()=>{
            onClose();
        }, 5000);

        return () => clearTimeout(timer);
    }, [onClose]);




    return (
        <div
            className={`toast align-items-center text-white ${style.toast} ${style[type]}`}
            role="alert"
            aria-live="assertive"
            aria-atomic="true"
        >
            <div className="d-flex">
                <div className="toast-body">
                    {type === "success" ? "✔️" : "❌"} {message}
                </div>
                <button
                    type="button"
                    className="btn-close btn-close-white me-2 m-auto"
                    aria-label="Close"
                    onClick={onClose}
                ></button>
            </div>
        </div>
    );
};