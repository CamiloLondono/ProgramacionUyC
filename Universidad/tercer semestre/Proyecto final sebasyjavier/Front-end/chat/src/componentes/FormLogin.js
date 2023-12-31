import React, { useState } from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import { obtenerUsuarios } from '../servicios/clienteaxios';
import EyeIcon from './EyeIcon';

const FormLogin = ({ handleUsuarioLogeado }) => {
  const [usuario, setUsuario] = useState('');
  const [contraseña, setContraseña] = useState('');
  const [mostrarContraseña, setMostrarContraseña] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();
  
    try {
      const usuarios = await obtenerUsuarios();
      const usuarioRegistrado = usuarios.find((user) => user.usuario === usuario && user.contraseña === contraseña);
      if (usuarioRegistrado) {
        // Inicio de sesión exitoso
        handleUsuarioLogeado(usuario);
        alert('Hola Estimado '+usuario+'\nInicio de sesión exitoso!');
      } else {
        // Credenciales inválidas
        alert('Credenciales inválidas');
      }
    } catch (error) {
      console.log(error);
    }
  };

  return (
    <div className="col-4">
      <form onSubmit={handleSubmit}>
        <div className="mb-3">
          <label htmlFor="usuario" className="form-label">Usuario</label>
          <input type="text" className="form-control" id="usuario" placeholder="Nombre de usuario" value={usuario} onChange={(e) => setUsuario(e.target.value)} />
        </div>
        <div className="mb-3">
          <label htmlFor="contraseña" className="form-label">Contraseña</label>
          <div className="input-group">
            <input
              type={mostrarContraseña ? "text" : "password"}
              className="form-control"
              id="contraseña"
              placeholder="Contraseña"
              value={contraseña}
              onChange={(e) => setContraseña(e.target.value)}
            />
            <span className="input-group-text" onClick={() => setMostrarContraseña(!mostrarContraseña)}>
              <EyeIcon />
            </span>
          </div>
        </div>
        <button type="submit" className="btn btn-success mx-3">
          Iniciar sesión
        </button>
      </form>
    </div>
  );
};

export default FormLogin;
