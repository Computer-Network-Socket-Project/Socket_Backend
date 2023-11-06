package org.springframework.modulith.runtime.autoconfigure;

import org.springframework.beans.factory.ListableBeanFactory;
import org.springframework.beans.factory.aot.BeanInstanceSupplier;
import org.springframework.beans.factory.config.BeanDefinition;
import org.springframework.beans.factory.support.RootBeanDefinition;
import org.springframework.boot.context.event.ApplicationStartedEvent;
import org.springframework.context.ApplicationContext;
import org.springframework.context.ApplicationListener;
import org.springframework.core.ResolvableType;
import org.springframework.modulith.runtime.ApplicationModulesRuntime;
import org.springframework.modulith.runtime.ApplicationRuntime;

/**
 * Bean definitions for {@link SpringModulithRuntimeAutoConfiguration}.
 */
public class SpringModulithRuntimeAutoConfiguration__TestContext001_BeanDefinitions {
  /**
   * Get the bean definition for 'springModulithRuntimeAutoConfiguration'.
   */
  public static BeanDefinition getSpringModulithRuntimeAutoConfigurationBeanDefinition() {
    RootBeanDefinition beanDefinition = new RootBeanDefinition(SpringModulithRuntimeAutoConfiguration.class);
    beanDefinition.setInstanceSupplier(SpringModulithRuntimeAutoConfiguration::new);
    return beanDefinition;
  }

  /**
   * Get the bean instance supplier for 'modulithsApplicationRuntime'.
   */
  private static BeanInstanceSupplier<SpringBootApplicationRuntime> getModulithsApplicationRuntimeInstanceSupplier(
      ) {
    return BeanInstanceSupplier.<SpringBootApplicationRuntime>forFactoryMethod(SpringModulithRuntimeAutoConfiguration.class, "modulithsApplicationRuntime", ApplicationContext.class)
            .withGenerator((registeredBean, args) -> SpringModulithRuntimeAutoConfiguration.modulithsApplicationRuntime(args.get(0)));
  }

  /**
   * Get the bean definition for 'modulithsApplicationRuntime'.
   */
  public static BeanDefinition getModulithsApplicationRuntimeBeanDefinition() {
    RootBeanDefinition beanDefinition = new RootBeanDefinition(SpringModulithRuntimeAutoConfiguration.class);
    beanDefinition.setTargetType(SpringBootApplicationRuntime.class);
    beanDefinition.setRole(BeanDefinition.ROLE_INFRASTRUCTURE);
    beanDefinition.setInstanceSupplier(getModulithsApplicationRuntimeInstanceSupplier());
    return beanDefinition;
  }

  /**
   * Get the bean instance supplier for 'modulesRuntime'.
   */
  private static BeanInstanceSupplier<ApplicationModulesRuntime> getModulesRuntimeInstanceSupplier(
      ) {
    return BeanInstanceSupplier.<ApplicationModulesRuntime>forFactoryMethod(SpringModulithRuntimeAutoConfiguration.class, "modulesRuntime", ApplicationRuntime.class)
            .withGenerator((registeredBean, args) -> SpringModulithRuntimeAutoConfiguration.modulesRuntime(args.get(0)));
  }

  /**
   * Get the bean definition for 'modulesRuntime'.
   */
  public static BeanDefinition getModulesRuntimeBeanDefinition() {
    RootBeanDefinition beanDefinition = new RootBeanDefinition(SpringModulithRuntimeAutoConfiguration.class);
    beanDefinition.setTargetType(ApplicationModulesRuntime.class);
    beanDefinition.setRole(BeanDefinition.ROLE_INFRASTRUCTURE);
    beanDefinition.setInstanceSupplier(getModulesRuntimeInstanceSupplier());
    return beanDefinition;
  }

  /**
   * Get the bean instance supplier for 'applicationModuleInitializingListener'.
   */
  private static BeanInstanceSupplier<ApplicationListener> getApplicationModuleInitializingListenerInstanceSupplier(
      ) {
    return BeanInstanceSupplier.<ApplicationListener>forFactoryMethod(SpringModulithRuntimeAutoConfiguration.class, "applicationModuleInitializingListener", ListableBeanFactory.class)
            .withGenerator((registeredBean, args) -> SpringModulithRuntimeAutoConfiguration.applicationModuleInitializingListener(args.get(0)));
  }

  /**
   * Get the bean definition for 'applicationModuleInitializingListener'.
   */
  public static BeanDefinition getApplicationModuleInitializingListenerBeanDefinition() {
    RootBeanDefinition beanDefinition = new RootBeanDefinition(SpringModulithRuntimeAutoConfiguration.class);
    beanDefinition.setTargetType(ResolvableType.forClassWithGenerics(ApplicationListener.class, ApplicationStartedEvent.class));
    beanDefinition.setRole(BeanDefinition.ROLE_INFRASTRUCTURE);
    beanDefinition.setInstanceSupplier(getApplicationModuleInitializingListenerInstanceSupplier());
    return beanDefinition;
  }
}
