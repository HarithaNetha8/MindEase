import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';

export default defineConfig({
  plugins: [react()],
  // Project uses index.html inside `src/` so set root there for Vite
  root: 'src',
});
