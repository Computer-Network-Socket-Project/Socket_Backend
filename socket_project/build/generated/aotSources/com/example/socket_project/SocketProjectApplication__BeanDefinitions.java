package com.example.socket_project;

import org.springframework.beans.factory.config.BeanDefinition;
import org.springframework.beans.factory.support.RootBeanDefinition;
import org.springframework.context.annotation.ConfigurationClassUtils;

/**
 * Bean definitions for {@link SocketProjectApplication}.
 */
public class SocketProjectApplication__BeanDefinitions {
  /**
   * Get the bean definition for 'socketProjectApplication'.
   */
  public static BeanDefinition getSocketProjectApplicationBeanDefinition() {
    RootBeanDefinition beanDefinition = new RootBeanDefinition(SocketProjectApplication.class);
    beanDefinition.setTargetType(SocketProjectApplication.class);
    ConfigurationClassUtils.initializeConfigurationClass(SocketProjectApplication.class);
    beanDefinition.setInstanceSupplier(SocketProjectApplication$$SpringCGLIB$$0::new);
    return beanDefinition;
  }
}
