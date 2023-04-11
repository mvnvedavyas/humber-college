import { getAuth } from 'firebase/auth';
import React from 'react';
import { useAuth } from '../../hooks/useAuth';
import { sendMessage } from '../../services/firebase';

function MessageInput({ roomId }: { roomId: string }) {
    const { currentUser: user } = getAuth();
    const [value, setValue] = React.useState('');

    const handleChange = (event: { target: { value: React.SetStateAction<string> } }) => {
        setValue(event.target.value);
    };

    const handleSubmit = (event: { preventDefault: () => void }) => {
        event.preventDefault();
        sendMessage(roomId, user!, value);
        setValue('');
    };

    if (roomId === 'announcements' &&
        (user?.uid !== 'Z99PiXuRASUFNALa51Em8SWn4E82' && user?.uid !== 'uY1p0xXYnpcVnkXRggpB7bcqoPH3')
    ) return null;

    return (
        <form onSubmit={handleSubmit} className="flex items-center justify-center">
            <input
                type="text"
                placeholder="Enter a message"
                value={value}
                onChange={handleChange}
                className="w-full p-4 text-gray-100 transition-colors duration-300 bg-gray-700 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                required
                minLength={1}
            />
            <button
                type="submit"
                disabled={Number(value) < 1}
                className="px-8 py-4 ml-4 text-gray-100 transition duration-300 bg-blue-700 rounded-md shadow-md hover:bg-blue-900 active:bg-blue-700 hover:cursor-pointer"
            >
                Send
            </button>
        </form>
    );
}

export { MessageInput };
