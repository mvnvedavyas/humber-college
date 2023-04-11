import ReactDOM from 'react-dom/client';
import App from './App';
import { AuthProvider } from './context/auth';
import './index.css';

const root = ReactDOM.createRoot(document.getElementById('root') as unknown as DocumentFragment);

root.render(
    <AuthProvider>
        <App />
    </AuthProvider>
);
